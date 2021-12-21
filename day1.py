import pandas as pd
import numpy as np

df = pd.read_csv('/Users/danielseal/Documents/py_files/adventofcode2021/data/day1.csv')
df["dydx"] = df["Depth"].diff(1)

# part 1
print(f'part1: {len(np.array(df["dydx"])[np.array(df["dydx"]) > 0])}')

df["trisum"] = [df.Depth.iloc[i] +  df.Depth.iloc[i+1] + df.Depth.iloc[i+2] for i in range(len(df)-2)] + [0, 0]
df["dydx2"] = df["trisum"].diff(1)

# part 2
print(f'part2: {len(np.array(df["dydx2"])[np.array(df["dydx2"]) > 0])}')