from collections import defaultdict, Counter
import numpy as np 
import itertools

instructions = {}
for idx, i in enumerate(open('/Users/danielseal/AOC_2021/data/day22_example3.txt', 'r').read().split('\n')):
    if i != '':
        instructions[f'{idx}-{i.split(" ")[0]}'] = [[e[0], [i for i in range(int(e[-1].split('..')[0]), int(e[-1].split('..')[-1])+1)]] for e in [p.split('=') for p in i.split(' ')[-1].split(',')]]

bound = 50
out_of_bounds = []
for k, v in instructions.items():
    mins, maxs = np.array((v[0][-1][0], v[1][-1][0], v[-1][-1][0])), np.array((v[0][-1][-1], v[1][-1][-1], v[-1][-1][-1]))
    if (any(mins < -1*bound)) | (any(maxs > bound)):
        out_of_bounds.append((k))

grid = defaultdict(lambda: 0)
for k, v in instructions.items():
    print('...')
    # if k not in out_of_bounds:
    coords = [(x,y,z) for x in v[0][-1] for y in v[1][-1] for z in v[-1][-1]]
    for coord in coords:
        if k.split('-')[-1] == 'on':
            grid[coord] = 1
        elif k.split('-')[-1] == 'off':
            grid[coord] = 0
        else:
            raise AssertionError('instruction is not on or off.')

# part 1
print(f'part1: {sum([v for _, v in grid.items()])}')


