import numpy as np

egrid = []
with open('/Users/danielseal/Documents/py_files/adventofcode2021/data/day11_example.txt') as f:
    for line in f.readlines():
        egrid.append([int(i) for i in list(line)[:-1]])
egrid = np.array(egrid)

def generate_NN(arr, i, j):
    coords = [(i+1, j), (i-1, j), (i, j+1), (i, j-1), (i-1, j-1), (i+1, j-1), (i-1, j+1), (i+1, j+1)]
    filtered = []
    for c in coords:
        if (c[0] == -1) | (c[0] == arr.shape[0]) | (c[1] == -1) | (c[1] == arr.shape[-1]):
            pass
        else:
            filtered.append(c)
    return filtered

flashes = 0 
step = 0
while step != 100:  # uncomment for part 1
# while np.sum(egrid) != 0:  # uncomment part 2 
    flashed = set() # store each flashed element
    egrid += 1  # add 1 to each element 
    flashing = np.where(egrid > 9) # elements to be flashed after step
    while len(flashing[0]) > 0: 
        for i, j in zip(flashing[0], flashing[1]):
            flashed.add((i, j))
            egrid[i, j] = 0
            neighbors = generate_NN(egrid,i,j)
            for n in neighbors:
                if (n[0], n[1]) not in flashed:
                    egrid[n[0], n[1]] += 1
        flashing = np.where(egrid > 9)
    flashes += len(flashed)
    step += 1

# part 1 + 2
print(f'Number of flashes = {flashes}, step = {step}')