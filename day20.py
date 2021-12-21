from collections import defaultdict
from copy import deepcopy

def cube(coord):
    i, j = coord[0], coord[-1]
    return [(i-1, j-1), (i-1, j), (i-1, j+1), 
            (i, j-1),   (i, j),   (i, j+1),
            (i+1, j-1), (i+1, j), (i+1, j+1)]

def bit_num(points, ima, point):
    b = []
    for c in cube(point):
        if points[f'{c[0]},{c[-1]}'] == '#':
            b.append('1')
        else:
            b.append('0')
    return ima[int(''.join(b), 2)]

def enhance(points, ima, sym='.'):
    new_points = defaultdict(lambda: sym) # initialise a new grid with sym (depends on ima (image enhancer))
    old_points = deepcopy(points)
    for point in old_points:
        r, c = int(point.split(',')[0]), int(point.split(',')[-1])
        for c in cube((r, c)):
            new_points[f'{c[0]},{c[-1]}'] = bit_num(points, ima, c)
    return new_points

def initialise(img):
    points = defaultdict(lambda: '.') # initialise a defaultdict with '.'
    for i in range(len(img)):
        for j in range(len(img[0])):
            points[f'{i},{j}'] = img[i][j]
    return points

def solve(img, ima, flip=False):
    points = initialise(img) # initialise img 
    iterations = 50 if flip else 2
    for i in range(iterations):
        if i % 2 == 0 or ima[0] == '.': # add in or to handle part 1 and    part 2
            sym = ima[0]
        else:
            sym = ima[-1] 
        points = enhance(points, ima, sym)
  
    return sum([1 for p in points if points[p] == '#'])

if __name__ == '__main__':
    
    all = []
    with open('/Users/danielseal/Documents/py_files/adventofcode2021/data/day20.txt') as f:
        for line in f.readlines():
            all.append(line[:-1])

    ima = ''.join(all[:all.index("")])
    img = [list(i) for i in all[all.index("")+1:]]

    print(f'part1: {solve(img, ima)}') 
    print(f'part2: {solve(img, ima, flip=True)}') 

