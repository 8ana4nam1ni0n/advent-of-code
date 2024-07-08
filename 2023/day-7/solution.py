from collections import Counter
from dataclasses import dataclass


class Strength:
    HighCard = 1
    OnePair = 2
    TwoPair = 3
    ThreeOfKind = 4
    FullHouse = 5
    FourOfKind = 6
    FiveOfKind = 7


CardStrength = {k:i+1 for i, k in enumerate("23456789TJQKA")}


@dataclass
class Hand:
    cards: str
    bid: int

    def strength(self) -> int:
        strength = Counter(self.cards)
        match sorted(strength.values(), reverse=True):
            case [5]: return Strength.FiveOfKind
            case [4, 1]: return Strength.FourOfKind
            case [3, 2]: return Strength.FullHouse
            case [3, 1, 1]: return Strength.ThreeOfKind
            case [2, 2, 1]: return Strength.TwoPair
            case [2, 1, 1, 1]: return Strength.OnePair
            case _: return Strength.HighCard

    def compare(self, other_hand: "Hand") -> int:
        if self.strength() > other_hand.strength():
            return 1
        if self.strength() < other_hand.strength():
            return -1

        for i in range(len(self.cards)):
            us = CardStrength[self.cards[i]]
            them = CardStrength[other_hand.cards[i]]
            if us > them:
                return 1
            if us < them:
                return -1
        # this should never happen?
        return 0

    def __gt__(self, other) -> bool:
        return self.compare(other) == 1

    def __lt__(self, other) -> bool:
        return self.compare(other) == -1

    def __eq__(self, other) -> bool:
        return self.compare(other) == 0


def parse_input(data: list[str]) -> list:
    return [Hand(cards=line.split()[0], bid=int(line.split()[1])) for line in data]


def get_hand_ranks(hands: list[Hand]) -> int:
    return sum((i+1) * hand.bid for i, hand in enumerate(sorted(hands)))


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Error: missing input")
        exit(1)

    filename = sys.argv[1]

    with open(filename, "r") as f:
        data = parse_input(f.read().splitlines())


    print(get_hand_ranks(data))


