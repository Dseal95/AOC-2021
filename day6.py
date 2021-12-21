import pandas as pd
import numpy as np
from collections import deque, Counter

df = pd.read_csv('/Users/danielseal/Documents/py_files/adventofcode2021/data/day6.csv')
fish = [int(i) for i in df.fish.iloc[0].split(',')]

def num_fish(fish: list, days: int):
    f = deque(Counter(fish)[i] for i in range(9))
    for _ in range(days):
        z = f.popleft() # remove 9s
        f[6] += z # add 0s to 6s
        f.append(z) # re-add the 0s 
    
    return sum(f)

# part 1 
print(f'part1: {num_fish(fish, days=80)}')
# part 2 
print(f'part2: {num_fish(fish, days=256)}')