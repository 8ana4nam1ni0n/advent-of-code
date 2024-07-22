import sys
from dataclasses import dataclass
from functools import reduce
from typing import TypeAlias


# solution 1
def hash_(string: str) -> int:
    return reduce(lambda cur, next: (cur + next) * 17 % 256, bytes(string, 'utf-8'), 0)


def solution_1(strings: list[str]) -> None:
    result = sum(map(hash_, strings))
    print(result)


# Used on Solution 2
@dataclass
class Lens:
    label: str
    length: int = 0

    def hash(self):
        return reduce(lambda cur, next: (cur + next) * 17 % 256, bytes(self.label, 'utf-8'), 0)

    def __eq__(self, other) -> bool:
        return other.label == self.label


Box: TypeAlias = list[Lens]


def parse_to_lens(string: str) -> Lens:
    if '=' in string:
        label, length = string.split('=')
        return Lens(label=label, length=int(length))
    else:
        return Lens(label=string[:-1])


def insert_lens(lens: Lens, box: Box) -> None:
    if lens in box:
        index = box.index(lens)
        box[index] = lens
    else:
        box.append(lens)


def remove_lens(lens: Lens, box: Box) -> None:
    if lens in box:
        box.remove(lens)


def get_lens_focusing_power(lens: Lens, slot: int) -> int:
    return (1 + lens.hash()) * slot * lens.length


def caluculate_focusing_power(box: Box) -> int:
    if len(box) == 0:
        return 0
    return sum(get_lens_focusing_power(lens, i + 1) for i, lens in enumerate(box))


def solution_2(strings: list[str]) -> None:
    hashmap = {i: [] for i in range(256)}
    lenses = [parse_to_lens(x) for x in strings]
    for lens in lenses:
        box = lens.hash()
        if lens.length > 0:
            insert_lens(lens, hashmap[box])
        else:
            remove_lens(lens, hashmap[box])

    focus_power = 0
    for v in hashmap.values():
        focus_power += caluculate_focusing_power(v)
    print(focus_power)


if __name__ == "__main__":
    filename = 'test'

    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename) as f:
        data = [ x.split(',') for x in f.read().splitlines() ][0]

    solution_1(data)
    solution_2(data)


