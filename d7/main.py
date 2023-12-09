CARDS = {
  'A': 14,
  'K': 13,
  'Q': 12,
  'J': 1,
  'T': 10
}

HANDS = {
  'high card': 0,
  'one pair': 1,
  'two pair': 2,
  'three of a kind': 3,
  'full house': 4,
  'four of a kind': 5,
  'five of a kind': 6,
}

def hand_type(hand):
  return hand.type

def cards_to_points(cards):
  pts = []
  for card in cards:
    if not card.isdigit():
      pts.append(CARDS[card])
    else:
      pts.append(int(card))
  return pts

class Hand:
  def __init__(self, line):
    self.cards = cards_to_points(line.strip().split()[0])
    self.bid = int(line.strip().split()[1])
    self.type = self.identify()

  def identify(self):
    jless = [x for x in self.cards if x != 1]
    grouped: Dict[int, List[int]] = {}
    for card in jless:
      if card not in grouped:
        grouped[card] = [card]
      else:
        grouped[card].append(card)
    grouped_counts = [len(grouped[x]) for x in grouped]
    if len(grouped_counts) == 0:
      return HANDS['five of a kind']
    elif len(grouped_counts) == 1:
      return HANDS['five of a kind']
    elif len(grouped_counts) == 2:
      if grouped_counts[0] == 1 or grouped_counts[1] == 1:
        return HANDS['four of a kind']
      else:
        return HANDS['full house']
    elif len(grouped_counts) == 3:
      if len(self.cards) - len(jless) == 1:
        return HANDS['three of a kind']
      if grouped_counts[0] == 2 or grouped_counts[1] == 2 or grouped_counts[2] == 2:
        return HANDS['two pair']
      else:
        return HANDS['three of a kind']
    elif len(grouped_counts) == 4:
      return HANDS['one pair']
    else:
      return HANDS['high card']


f=open("input.txt", "r")
hands = []
for line in f.readlines():
  hands.append(Hand(line))
hands.sort(key=lambda x: (hand_type(x), tuple(x.cards)), reverse=True)
for hand in hands:
  print(f"{[key for key, value in HANDS.items() if value == hand.type]} {hand.cards}")
sum = 0
for i in range(len(hands)):
  sum += (len(hands) - i) * hands[i].bid
print(f"sum: {sum}")