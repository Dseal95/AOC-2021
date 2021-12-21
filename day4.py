import pandas as pd
import numpy as np

cards = []
with open('/Users/danielseal/Documents/py_files/adventofcode2021/data/day4_example.txt') as f:
    for i, line in enumerate(f.readlines()):
        if i == 0:
            numbers = line[:-1]
        else:
            cards.append(line[:-1])
numbers = [int(n) for n in numbers.split(',')]
cards = [cards[i: j] for i, j in list(zip(np.arange(1, len(cards)+1, 6), np.arange(6, len(cards)+1, 6)))]

def create_card(cards, i):
    cleaned = []
    for c in [i.split(' ') for i in cards[i]]:
        e = []
        for a in c:
            if a != '':
                e.append(int(a))
        cleaned.append(e)
    return np.array(cleaned)

cards_ = []
for i in range(len(cards)):
    cards_.append(create_card(cards, i))

def update_card(card, loc):
    card[loc] = -1
    return card

def check_card(card):
    row = [True for i in card.sum(axis=0) if i == -5]
    col = [True for i in card.sum(axis=1) if i == -5]
    if (len(row) > 0) | (len(col) > 0):
        return True
    else:
        return False

winner = []
for n in numbers:
    for idx, card in enumerate(cards_):
        # find location of number 
        loc = [(i, j) for i in range(5) for j in range(5) if card[i, j] == n]
        for l in loc:
            # update card 
            card = update_card(card, l)
        # switch updated card with previous card 
        cards_[idx] = card
        if check_card(card):
            # print(card, n )
            winner.append([idx, n, sum(card[card!= -1]) * n])

# part 1         
print(f'part1: {winner[0][-1]}')


ws = [False]*len(cards_)
loser = []
for i in winner:
    ws[i[0]] = True
    if ws.count(False) == 0:
        loser.append(i)

# part 2 
print(f'part2: {loser[0][-1]}') 