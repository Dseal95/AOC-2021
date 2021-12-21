import pandas as pd
import numpy as np

df = pd.read_csv('/Users/danielseal/Documents/py_files/adventofcode2021/data/day2.csv')

print(df.head())

# part 1 
h = sum([int(i.split(' ')[-1]) for i in df.moves.to_list() if i.split(' ')[0] == 'forward'])
up = sum([-int(i.split(' ')[-1]) for i in df.moves.to_list() if i.split(' ')[0] == 'up'])
down = sum([int(i.split(' ')[-1]) for i in df.moves.to_list() if i.split(' ')[0] == 'down'])
d = up + down

print(f'part1: {d * h}')

# part 2
a, h2, d2 = 0, 0, 0
for i in df.moves.to_list():
    w, m = i.split(' ')[0], int(i.split(' ')[-1])
    if w == 'down':
        a+=m
    if w == 'up':
        a-=m
    if w == 'forward':
        h2+=m
        d2+=(a*m)
    else: 
        pass

print(f'part2: {d2*h2}')
