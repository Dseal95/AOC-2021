from collections import defaultdict

def update_polymer(polymer, insertion_rules, steps):
    result_dict = {k: 0 for k in insertion_rules.keys()}
    for i in range(len(polymer) - 1):
        result_dict[polymer[i:i + 2]] += 1  # identify inserts
    for _ in range(steps):
        for k, v in [[k, v] for k, v in result_dict.items() if v > 0]: # filter through all valid inserts
            # identify insertions for next step
            result_dict[k[0] + insertion_rules[k]] += v   
            result_dict[insertion_rules[k] + k[-1]] += v
            result_dict[k] -= v  # minus this insertions as completed
    return result_dict

def solve(polymer, rules, steps):
    result = update_polymer(polymer, rules, steps)
    # count letter frequencies
    freq = defaultdict(int)
    for k, v in result.items():
        freq[k[0]] += v
        freq[k[-1]] += v
    # fix double counting:
    freq[polymer[0]] += 1  # 1st and last letter not double counted
    freq[polymer[-1]] += 1  
    freq.update((k, v // 2) for k, v in freq.items())
    return max([v for _, v in freq.items()]) - min([v for _, v in freq.items()])


if '__main__' == __name__:
    
    rules = defaultdict(int)
    with open('/Users/danielseal/Documents/py_files/adventofcode2021/data/day14.txt') as f:
        for line in f.readlines():
            if len(line[:-1].split("->")) > 1:
                rules[line[:-1].split("->")[0].lstrip().rstrip()] = line[:-1].split("->")[-1].lstrip().rstrip()
            else:
                if len(line[:-1]) != 0:
                    polymer = line[:-1]

    # part 1 + 2
    print(f'part1: {solve(polymer, rules, 10)}')
    print(f'part2: {solve(polymer, rules, 40)}')