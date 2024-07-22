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
    length: int | None = None

    def is_remove(self):
        return not self.length

    def hash(self):
        return reduce(lambda cur, next: (cur + next) * 17 % 256, bytes(self.label, 'utf-8'), 0)


Box: TypeAlias = list[Lens]


def parse_to_lens(string: str) -> Lens:
    if '=' in string:
        label, length = string.split('=')
        return Lens(label=label, length=int(length))
    else:
        return Lens(label=string[:-1])


def remove_lens(lens: Lens, box: Box) -> None:
    pass



def solution_2(strings: list[str]) -> None:
    hashmap = {i: [] for i in range(256)}
    pass


if __name__ == "__main__":
    filename = 'test'

    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename) as f:
        data = [ x.split(',') for x in f.read().splitlines() ][0]

    solution_1(data)


