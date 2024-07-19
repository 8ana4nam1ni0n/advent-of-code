from typing import TypeAlias

Grid: TypeAlias = list[list[str]]
ImmutableGrid: TypeAlias = tuple[tuple[str, ...], ...]


def print_grid(grid: Grid) -> None:
    for r in grid:
        print(''.join(r))


def move_north(grid: Grid) -> Grid:
    for i in range(1, len(grid)):
        for j in range(len(grid[0])):
            current_row = i
            if grid[current_row][j] == 'O':
                while current_row > 0 and grid[current_row-1][j] == '.':
                    grid[current_row][j], grid[current_row-1][j] = '.', 'O'
                    current_row -= 1
    return grid


def calculate_load(grid: Grid) -> int:
    load = 0
    for i, row in enumerate(grid[::-1]):
        load += row.count('O') * (i + 1)
    return load

# Solution 1
def solution_1(grid: Grid) -> int:
    return calculate_load(move_north(grid))


# Solution 2
def rotate_clockwise(grid: Grid) -> Grid:
    return [list(row) for row in zip(*grid[::-1])]

# Perform a cycle: north, west, south, east
def perform_cycle(grid: Grid) -> Grid:
    g = deep_copy(grid)
    for _ in range(4):
        g = move_north(g)
        g = rotate_clockwise(g)
    return g

def deep_copy(grid: Grid | ImmutableGrid) -> Grid:
    return [[*row] for row in grid]


def to_immutable(grid: Grid) -> ImmutableGrid:
    return tuple(tuple(row) for row in grid)


def get_repeated_cycle(grid: Grid, max_cycles=1_000_000_000) -> tuple[Grid, int, int]:
    seen = {}

    g = deep_copy(grid)
    for cycle in range(1, max_cycles):
        g = perform_cycle(g)
        i_g = to_immutable(g)
        if i_g in seen:
            cycle_len = cycle - seen[i_g]
            return (g, cycle, cycle_len)
        seen[i_g] = cycle

    return (g, -1, -1)

def solution_2(grid: Grid) -> int:
    g, cycle_start, cycle_length = get_repeated_cycle(grid)
    cycles = (1_000_000_000 - cycle_start) % cycle_length

    for _ in range(cycles):
        g = perform_cycle(g)

    return calculate_load(g)


if __name__ == "__main__":
    import sys

    filename = 'test'
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename) as f:
        grid = [[*x] for x in f.read().splitlines()]


    print(solution_1(grid))
    print(solution_2(grid))

