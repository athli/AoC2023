from operator import attrgetter

class CamelHand:

    vals = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2
    }

    def __init__(self, _hand, _bid):
        self.hand = (_hand)
        self.cards = list(self.hand)
        self.bid = int(_bid)
        self.level = 0

    def __lt__(self,other):
        if self.level < other.level:
            return True
        elif self.level > other.level:
            return False
        else:
            for i in range(len(self.cards)):
                if CamelHand.vals[self.cards[i]] < CamelHand.vals[other.cards[i]]:
                    return True
                elif CamelHand.vals[self.cards[i]] > CamelHand.vals[other.cards[i]]:
                    return False
            return False

    def findlevel(self):
        counts = {}
        for card in self.cards:
            if card not in counts.keys():
                counts[card] = 1
            else:
                counts[card] += 1
        level = max(counts.values())
        if level == 3 and 2 in counts.values():
            self.level = 3.5
        elif level == 2 and len(counts.values()) == 3:
            self.level = 2.5
        else:
            self.level = level
 
def camelHandWinnings(filename):
    hands = []
    with open(filename) as f:
        for line in f:
            hands.append(CamelHand(line.split()[0], int(line.split()[1])))
    for hand in hands:
        hand.findlevel()
    sortedHands = sorted(hands)
    total = 0
    for i in range(len(sortedHands)):
        total += (i + 1) * sortedHands[i].bid
    return total

print(camelHandWinnings('day7input.txt'))