import numpy as np

hm = []
with open('/Users/danielseal/Documents/py_files/adventofcode2021/data/day9_example.txt') as f:
    for line in f.readlines():
        hm.append([int(i) for i in list(line)[:-1]])
hm = np.array(hm)

def generate_NN(arr, i, j):
    coords = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
    filtered = []
    for c in coords:
        if (c[0] == -1) | (c[0] == arr.shape[0]) | (c[1] == -1) | (c[1] == arr.shape[-1]):
            pass
        else:
            filtered.append(c)
    return filtered

def lowest_check(hm, coords, start):
    if all([hm[c] for c in coords] > hm[start]):
        return start

lp = []
for i in range(hm.shape[0]):
    for j in range(hm.shape[-1]):
        coords = generate_NN(hm, i, j)
        lp.append(lowest_check(hm, coords=coords, start=(i, j)))

# part 1 Answer
print(f'part1: {sum([hm[c]+1 for c in lp if c is not None])}')

# part 2:
def network(arr, coords, N):
    coords = [c for c in [c for c in generate_NN(arr, coords[0], coords[1]) if arr[c] != 9] if c not in N]
    N += coords
    for coord in coords:
        network(arr=hm, coords=coord, N=N)

    return N

buckets = [c for c in lp if c is not None]
res = []
for b in buckets:
    a = network(arr=hm, coords=b, N=[b])
    res.append(len(a))

# Part 2 Answer
print(f'part2: {np.prod(sorted(res, reverse=True)[:3])}')
