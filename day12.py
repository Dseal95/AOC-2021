from itertools import chain
from collections import Counter , deque

input = []
with open('/Users/danielseal/Documents/py_files/adventofcode2021/data/day12.txt') as f:
    for line in f.readlines():
        input.append((line.split('-')[0], line.split('-')[-1][:-1]))


def create_graph(input):
    g = {i: [] for i in (sorted(set(chain.from_iterable(input)), reverse=True))}
    for i in input:
        g[i[0]].append(i[-1])
        g[i[-1]].append(i[0])
    return g


def find_all_paths(graph, start, end, path=[], not_allowed=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node_allowed(graph, path, node):
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths  


if '__main__' == __name__:

    part = "2"

    if part == "1":
        # part 1 condition
        def node_allowed(graph, path, node):
            small_caves = [k for k, _ in graph.items() if k == k.lower()]
            d = Counter([e for e in path if e in small_caves])
            if (d[node] < 1):
                return True
            else:
                return False

        paths = find_all_paths(create_graph(input), 'start', 'end', [])
        print(f'part1: {len(paths)}')

    else:
        #  part 2 condition
        def node_allowed(graph, path, node):
            small_caves = [k for k, _ in graph.items() if k == k.lower() if k not in ["start", "end"]]
            d = Counter([e for e in path if e in small_caves])
            if (node == "start"):
                return False
            if (node not in d):
                return True
            if (d[node] == 1) & (len([(k, v) for k, v in d.items() if k!=node if v == 2]) == 0):
                return True
            return False

        paths = find_all_paths(create_graph(input), 'start', 'end', [])
        print(f'part2: {len(paths)}')

