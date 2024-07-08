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
CardStrengthWithWildcard = {k:i+1 for i, k in enumerate("J23456789TQKA")}


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

    def strength_with_wildcard(self) -> int:
        strength = Counter(self.cards)
        wild_cards_count = strength.pop('J', 0)
        match (sorted(strength.values(), reverse=True), wild_cards_count):
            case ([5], _) | ([4], 1) | ([3], 2) | ([2], 3) | ([1], 4) |([], 5):
                return Strength.FiveOfKind
            case ([4, 1], _) | ([3, 1], 1) | ([2, 1], 2) | ([1 , 1], 3):
                return Strength.FourOfKind
            case ([3, 2], _) | ([2, 2], 1):
                return Strength.FullHouse
            case ([3, 1, 1], _) | ([2, 1, 1], 1) | ([1, 1, 1], 2):
                return Strength.ThreeOfKind
            case ([2, 2, 1], _):
                return Strength.TwoPair
            case ([2, 1, 1, 1], _) | ([1,1,1,1], 1):
                return Strength.OnePair
            case _:
                return Strength.HighCard



    def compare(self, other_hand: "Hand") -> int:

        if self.strength() == other_hand.strength():
            for i in range(len(self.cards)):
                us = CardStrength[self.cards[i]]
                them = CardStrength[other_hand.cards[i]]
                if us != them:
                    return us - them

        return self.strength() - other_hand.strength()

    def compare_with_wildcard(self, other_hand: "Hand") -> int:

        if self.strength_with_wildcard() == other_hand.strength_with_wildcard():
            for i in range(len(self.cards)):
                us = CardStrengthWithWildcard[self.cards[i]]
                them = CardStrengthWithWildcard[other_hand.cards[i]]
                if us != them:
                    return us - them

        return self.strength_with_wildcard() - other_hand.strength_with_wildcard()

    # def __gt__(self, other) -> bool:
    #     return self.compare(other) > 0
    #
    # def __lt__(self, other) -> bool:
    #     return self.compare(other) < 0
    #
    # def __eq__(self, other) -> bool:
    #     return self.compare(other) == 0

    def __gt__(self, other) -> bool:
        return self.compare_with_wildcard(other) > 0

    def __lt__(self, other) -> bool:
        return self.compare_with_wildcard(other) < 0

    def __eq__(self, other) -> bool:
        return self.compare_with_wildcard(other) == 0


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


    # solution 1
    # print(get_hand_ranks(data))

    #solution 2
    print(get_hand_ranks(data))


