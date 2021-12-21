import pandas as pd
import numpy as np

df = pd.read_csv('/Users/danielseal/Documents/py_files/adventofcode2021/data/day5.csv')

df["x1"] = [int(df.line.iloc[i].split(' -> ')[0].split(',')[0]) for i in range(len(df))]
df["y1"] = [int(df.line.iloc[i].split(' -> ')[0].split(',')[-1]) for i in range(len(df))]
df["x2"] = [int(df.line.iloc[i].split(' -> ')[-1].split(',')[0]) for i in range(len(df))]
df["y2"] = [int(df.line.iloc[i].split(' -> ')[-1].split(',')[-1]) for i in range(len(df))]
df["h/v"] = np.where((df.x1 == df.x2) | (df.y1 == df.y2), 1, 0)

arr = np.zeros((max([max(df.x1), max(df.x2)])+1, max([max(df.y1), max(df.y2)])+1))

def generate_line_coords(x1, x2, y1, y2):
    dx = abs(x2) - abs(x1)
    dy = abs(y2) - abs(y1)
    if (dx != 0) & (dy == 0):
        xs = [i for i in range(np.sort([x1, x2])[0], np.sort([x1, x2])[-1]+1)]
        ys = [y1]*len(xs)
        coords = list(zip(xs, ys))
    if (dx == 0) & (dy != 0):
        ys = [i for i in range(np.sort([y1, y2])[0], np.sort([y1, y2])[-1]+1)]
        xs = [x1]*len(ys)

    return list(zip(xs, ys))


def generate_diagonal_coords(x1, x2, y1, y2):
    # y coords
    dy = y2 - y1 
    if dy > 0:
         ys = [i for i in range(y1, y2+1, +1)]
    else:
         ys = [i for i in range(y1, y2-1, -1)]
    # x coords 
    dx = x2 - x1
    if dx > 0:
        xs = [i for i in range(x1, x2+1, +1)]
    else:
        xs = [i for i in range(x1, x2-1, -1)]

    return list(zip(xs, ys))

# for idx, row in df[df["h/v"] == 1].iterrows(): # uncomment for part 2 
for idx, row in df.iterrows():
    if row['h/v'] == 1:
        coords = generate_line_coords(row.y1, row.y2, row.x1, row.x2)
    else:
        coords = generate_diagonal_coords(row.y1, row.y2, row.x1, row.x2)
    # update array  
    for c in coords:
        arr[c] += 1

# part 1 or 2 
print(len(arr[arr >= 2]))

