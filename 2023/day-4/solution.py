import math
from dataclasses import dataclass


@dataclass
class Card:
    id: int
    win_nums: set[str]
    play_nums: set[str]

    def get_card_score(self):
        return math.floor(2**(len(self.win_nums & self.play_nums) - 1))

    def matches(self):
        return len(self.win_nums & self.play_nums)

def parse_input(data: list[str]) -> list[Card]:
    cards = []
    for d in data:
        id = int(d.split(':')[0].split()[-1])
        win_nums, play_nums = d.split(':')[1].split('|')
        win_nums = set(win_nums.split())
        play_nums = set(play_nums.split())
        cards.append(Card(id=id, win_nums=win_nums, play_nums=play_nums))
    return cards

# solution 2
def get_total_instances(current, data, memo={}):

    key = tuple(current)
    if key in memo:
        return memo[key]

    if len(current) == 0:
        return 0

    total = 0
    for i, matches in current:
        sublist = data[i:i+matches]
        total += get_total_instances(sublist, data, memo) + 1

    memo[key] = total
    return memo[key]



if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("missing input")
        exit(1)

    data_file = sys.argv[1]

    with open(data_file, "r") as f:
        data = f.read().splitlines()

    # solution 1
    cards = parse_input(data)
    print(sum(card.get_card_score() for card in cards))

    # solution 2
    scratchcards = [(card.id,card.matches()) for card in cards]
    print(get_total_instances(scratchcards, scratchcards))






