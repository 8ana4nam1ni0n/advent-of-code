from typing import TypeAlias

Grid: TypeAlias = list[str]


def has_symmetry(grid: Grid, idx: int) -> bool:
    current = idx
    next = idx + 1

    while current >= 0 and next < len(grid):
        if grid[current] != grid[next]:
            return False
        current -= 1
        next += 1

    return True


def find_symmetrical_line(grid: Grid) -> int:
    for i in range(len(grid) - 1):
        if has_symmetry(grid, i):
            return i + 1
    return 0


def solution_1(grids: list[Grid]) -> int:
    result = 0
    for grid in grids:
        horizontal = find_symmetrical_line(grid)
        vertical = find_symmetrical_line(list(zip(*grid)))

        result += vertical
        result += 100 * horizontal

    return result


def can_fix_smudge(current: str, next: str):
    fixed_smudges = 0
    for x, y in zip(current, next):
        if x != y:
            fixed_smudges += 1
        if fixed_smudges > 1:
            return False
    return fixed_smudges == 1



def has_symmetry_with_smudge(grid: Grid, idx: int) -> bool:
    current = idx
    next = idx + 1
    still_reflective = False

    while current >= 0 and next < len(grid):
        if grid[current] != grid[next]:
            if still_reflective:
                return not still_reflective
            if can_fix_smudge(grid[current], grid[next]):
                still_reflective = True
            else:
                return False

        current -= 1
        next += 1

    return still_reflective


def find_symmetrical_line_2(grid: Grid) -> int:
    for i in range(len(grid) - 1):
        if has_symmetry_with_smudge(grid, i):
            return i + 1
    return 0


def solution_2(grids: list[Grid]) -> int:
    result = 0
    for grid in grids:
        horizontal = find_symmetrical_line_2(grid)
        vertical = find_symmetrical_line_2(list(zip(*grid)))

        result += vertical
        result += 100 * horizontal

    return result


if __name__ == "__main__":
    import sys

    filename = 'test'

    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename) as f:
        data = f.read()

    grids = [d.split() for d in data.split('\n\n')]
    print(solution_1(grids))
    print(solution_2(grids))


