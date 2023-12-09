from math import pow
from copy import copy


class Card:
    def __init__(self, line):
        split = line.split()
        self.id = int(split[1][:-1])
        self.winning = []
        self.my = []
        self.point = 0
        win = True
        for i in split:
            if len(i) == 0:
                continue
            if i == '|':
                win = False
                continue
            if i[-1] == '\n':
                self.my.append(int(i[:-1]))
                break
            if i.isdigit():
                if win:
                    self.winning.append(int(i))
                else:
                    self.my.append(int(i))

    def calculate(self):
        count = 0
        for i in self.my:
            if i in self.winning:
                count += 1
        if count == 0:
            return 0
        return count


def expand_cards(lst):
    cards = copy(lst)
    for card in cards:
        # print(f"for card {card.id}")
        count = card.calculate()
        for i in range(count):
            if card.id + i >= len(lst):
                break
            # print(f"adding card {lst[card.id + i].id}")
            cards.append(copy(lst[card.id + i]))
    return len(cards)

f = open("input.txt", "r")
cards = []
for line in f.readlines():
    cards.append(Card(line))
print(f"count: {expand_cards(cards)}")
