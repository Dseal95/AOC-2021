from collections import Counter
import itertools
from functools import lru_cache

s1, s2, _ = open('/Users/danielseal/Documents/py_files/adventofcode2021/data/day21_example.txt', 'r').read().split('\n')
s1, s2 = int(s1.split(': ')[-1]), int(s2.split(': ')[-1])

def part1(s1, s2, end_score: int):
    die = [1,2,3]
    turns = 0
    p1, p2, score1, score2 = s1, s2, 0, 0
    while (score1 < end_score) & (score2 < end_score):
        if turns%2 == 0: # p1 goes
            p1 += sum(die)
            if (p1 > 10):
                p1 %= 10
            if p1%10==0:
                p1=10
            score1 += p1
        elif turns%2==1: # p2 goes 
            p2 += sum(die)
            if p2 > 10:
                p2 %= 10
            if p2%10==0:
                p2=10
            score2 += p2
        else:
            raise AssertionError("turn not a number.")

        die = [die[-1]+1, die[-1]+2, die[-1]+3]
        die = [d%100 for d in die]
        try:
            die[die.index(0)] = 100
        except ValueError:
            pass
        
        turns += 1

    return (turns*3) * min(score1, score2)
    
# part 1
print(f'part1: {part1(s1, s2, 1000)}')

# part 2
# possible outcomes each roll i.e. a 3 can happen once there are 3x1s...
poss_rolls = [x for x in itertools.product((1,2,3), repeat=3)]
end_score = 21

@lru_cache(maxsize=None)  # saves the return value of the function called
def dirac(p1_pos, p1_score, p2_pos, p2_score):
    global poss_rolls, end_score
    if p1_score >= end_score:
        return 1, 1
    elif p2_score >= end_score:
        return 0, 1
    else:
        p1wins = 0
        total = 0
        for roll in poss_rolls:
            curr_p1_pos = (p1_pos + sum(roll)) % 10 or 10  # return 10 if N%10 is 0
            curr_p1_score = p1_score + curr_p1_pos
            p2wins, subtotal = dirac(p2_pos, p2_score, curr_p1_pos, curr_p1_score) # swap scores to simulate alternating p1 and p2 goes 
            total += subtotal
            p1wins += (subtotal - p2wins)
        
        return (p1wins, total)

def part2(p1_pos, p2_pos, end_score):
    p1wins, total = dirac(p1_pos, 0, p2_pos, 0)
    return max(p1wins, total - p1wins)

print(f"part2: {part2(s1, s2, 21)}")