import pandas as pd
import numpy as np
from collections import Counter

# part 1
cols = {i: [] for i in range(12)}
bits = []
with open('/Users/danielseal/Documents/py_files/adventofcode2021/data/day3.txt') as f:
    for line in f.readlines():
        bits.append(line[:-1])
        for idx, e in enumerate(line):
            if idx < 12:
                cols[idx].append(e)
gamma, epsilon = [], []
for k in cols:
    gamma.append(Counter(cols[k]).most_common()[0][0])
    epsilon.append(Counter(cols[k]).most_common()[-1][0])

gamma, epsilon = ''.join(gamma), ''.join(epsilon)
print(int(gamma, 2) * int(epsilon, 2))

# part 2 - run twice for o2 and co2
bits = np.array(bits)
for idx in range(len(bits[0])):
    c =  [b[idx] for b in bits]
    mc, lc = Counter(c).most_common()[0], Counter(c).most_common()[-1]
    if mc[-1] == lc[-1]:
        idxs = [i for i, e in enumerate(c) if e == '0']
    else:
        idxs = [i for i, e in enumerate(c) if e == lc[0]]
    # update bits 
    bits = bits[idxs]

o2 = '011010001111'
co2 = '111001000000'
print(int(o2, 2) * int(co2, 2))



