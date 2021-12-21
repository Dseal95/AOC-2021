import matplotlib.pyplot as plt
import numpy as np 

input = []
folds = []
with open('/Users/danielseal/Documents/py_files/adventofcode2021/data/day13.txt') as f:
    for line in f.readlines():
        if line[:-1].split(' ')[0] == 'fold':
            folds.append(line[:-1].split(' ')[-1].split("="))
        else:
            input.append(line[:-1])
input = [(int(i.split(',')[-1]), int(i.split(',')[0])) for i in input if i != '']  # flip x and y 

arr = np.zeros((max([i[0] for i in input])+1 , max([i[-1] for i in input])+1))
for coord in input:
    arr[coord] = -1

def update_array(arr, diff):
    zeros = np.zeros((diff, arr.shape[-1]))
    return np.concatenate([arr, zeros])

def fold(arr, f):
    if f[0] == 'y':
        h1 = arr[: int(f[-1])]
        h2 = arr[ int(f[-1]) + 1 :]
        # handle uneven folds by resizing arrays using 0s
        if h1.shape[0] != h2.shape[0]:
            if h2.shape[0] < h1.shape[0]:
                h2 = update_array(h2, diff=h1.shape[0]-h2.shape[0])
            else:
                h1 = update_array(h1, diff=h2.shape[0]-h1.shape[0])
        return h1 + h2[::-1]
    if f[0] == "x":
        arr = arr.T
        h1 = arr[: int(f[-1])]
        h2 = arr[int(f[-1])+1:]
        # handle uneven folds by resizing arrays using 0s
        if h1.shape[0] != h2.shape[0]:
            if h2.shape[0] < h1.shape[0]:
                h2 = update_array(h2, diff=h1.shape[0]-h2.shape[0])
            else:
                h1 = update_array(h1, diff=h2.shape[0]-h1.shape[0])
        return (h1 + h2[::-1]).T

# part 1 + 2
for idx, f in enumerate(folds):
    arr = fold(arr, f)
    if idx == 0:
        print(f'part1: {len(arr[arr < 0])}')

# part 2
plt.imshow(arr < 0)
plt.show()

