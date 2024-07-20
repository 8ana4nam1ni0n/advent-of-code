from typing import TypeAlias

Group: TypeAlias = tuple[int, ...]
HotSpringRecord: TypeAlias = tuple[str, Group]


def parse_data(data: list[str]) -> list[HotSpringRecord]:
    records: list[HotSpringRecord] = []
    for record in data:
        hotspring, groups = record.split()
        groups = tuple(map(int, groups.split(',')))
        # append dots at start and end of hotspring to eliminate edge cases
        # that ocurr when broken springs are at the edges of the string
        records.append(('.' + hotspring + '.', groups))
    return records

def unfold(hotsprings: list[HotSpringRecord]) -> list[HotSpringRecord]:
    unfolded_records: list[HotSpringRecord] = []
    for record, group in hotsprings:
        unfolded_records.append(('.' + '?'.join([record[1:-1]] * 5) + '.', group * 5))
    return unfolded_records


def group_fits(hotspring: str, start: int, end: int) -> bool:
    if start - 1 < 0 or end + 1 >= len(hotspring):
        return False

    if hotspring[start - 1] == '#' or hotspring[end + 1] == '#':
        return False

    if '#' in hotspring[:start]:
        return False

    if '.' in hotspring[start:end + 1]:
        return False

    return True

def get_possible_combinations(hotspring: str, groups: Group, memo={}) -> int:
    if (hotspring, groups) in memo:
        return memo[(hotspring, groups)]

    if not groups:
        return 0 if '#' in hotspring else 1

    combinations = 0
    for i in range(len(hotspring)):
        start = i - (groups[0] - 1)
        if group_fits(hotspring, start, i):
            combinations += get_possible_combinations(hotspring[i+1:], groups[1:], memo)
    memo[(hotspring, groups)] = combinations
    return combinations

def solution_1(hotspring_records: list[HotSpringRecord]) -> int:
    result = 0
    for hotspring, group in hotspring_records:
        result += get_possible_combinations(hotspring, group)
    return result

def solution_2(hotspring_records: list[HotSpringRecord]) -> int:
    return solution_1(hotspring_records)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Error: missing input")
        exit(1)

    filename = sys.argv[1]

    with open(filename) as f:
        data = f.read().splitlines()

    hotsprings = parse_data(data)
    print(solution_1(hotsprings))
    print(solution_2(unfold(hotsprings)))
