import numpy as np 
from itertools import chain

nav = []
with open('/Users/danielseal/Documents/py_files/adventofcode2021/data/day10.txt') as f:
    for line in f.readlines():
        nav.append(line[:-1])

def reduce(l, lold):
    if len(l) == len(lold):
        return np.array(l) 
    chunks = list(chain.from_iterable([[i, i+1] for i in range(len(l) - 1) if (l[i] + l[i+1]) == 0 if l[i] > 0]))
    lold = l
    l = [l[i] for i in range(len(l)) if i not in chunks]
    return reduce(l, lold)

mapping = {'(': 1, ')': -1, '[': 2, ']': -2, '{': 3, '}': -3, '<': 4, '>': -4}
points = {1: 3, 2:57, 3:1197, 4:25137}
score, completion = [], []
for n in nav:
    mapped = [*map(mapping.get, n)]
    res = reduce(l=mapped, lold=mapped+[0])
    if len(res[res < 0]) != 0:
        # corrupt
        score.append([points[abs(res[i+1])] for i in range(len(res)-1) if res[i] > 0 if res[i+1] < 0][0])
    else:
        # incomplete
        s = 0
        for v in [i for i in res[::-1]]:
            s = ((s*5) + v)
        completion.append(s)

# part 1 
print(f'part1: {sum(score)}')
# part 2
print(f'part2: {sorted(completion)[len(completion)//2]}')
