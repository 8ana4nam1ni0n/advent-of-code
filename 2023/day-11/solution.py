from itertools import combinations
from typing import TypeAlias

Grid: TypeAlias = list[list[str]]
Galaxy: TypeAlias = tuple[int,int]
GalaxyPair: TypeAlias = tuple[Galaxy, Galaxy]

def get_expansion_indeces(universe: Grid) -> dict[str, int]:
    expansion_indecies = {}

    expansion_indecies['row'] = []
    for i, row in enumerate(universe):
        if all(r == '.' for r in row):
            expansion_indecies['row'].append(i)

    expansion_indecies['col'] = []
    for i in range(len(universe[0])):
        if all(r[i] == '.' for r in universe):
            expansion_indecies['col'].append(i)

    return expansion_indecies


def get_galaxies_coordinates(universe: Grid, expand_idx, expansion_factor=2):
    galaxies = []
    for i, row in enumerate(universe):
        for j, col in enumerate(row):
            if col == '#':
                rows_to_expand = len([x for x in expand_idx['row'] if i > x])
                cols_to_expand = len([x for x in expand_idx['col'] if j > x])
                galaxies.append((abs(i + rows_to_expand * (expansion_factor - 1)), abs(j + cols_to_expand * (expansion_factor - 1))))

    return galaxies


def get_galaxy_distance(g1: Galaxy, g2: Galaxy) -> int:
    (x1, y1), (x2, y2) = g1, g2
    return abs(x2 - x1) + abs(y2 - y1)


def get_galaxy_pairs(galaxies: list[Galaxy]) -> list[GalaxyPair]:
    return list(combinations(galaxies, 2))


def solution_1(universe: Grid) -> int:
    expansion_idx = get_expansion_indeces(universe)
    galaxies = get_galaxies_coordinates(universe, expansion_idx)
    galaxy_pairs = get_galaxy_pairs(galaxies)
    shortest_paths = []

    for g1, g2 in galaxy_pairs:
        shortest_paths.append(get_galaxy_distance(g1, g2))

    return sum(shortest_paths)


def solution_2(universe: Grid) -> int:
    expansion_idx = get_expansion_indeces(universe)
    galaxies = get_galaxies_coordinates(universe, expansion_idx, expansion_factor=1_000_000)
    galaxy_pairs = get_galaxy_pairs(galaxies)
    shortest_paths = []

    for g1, g2 in galaxy_pairs:
        shortest_paths.append(get_galaxy_distance(g1, g2))

    return sum(shortest_paths)
def print_grid(grid: Grid) -> None:
    for g in grid:
        print(g)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Error: missing input")
        exit(1)

    filename = sys.argv[1]

    with open(filename) as f:
        universe = [' '.join(x).split() for x in f.read().splitlines()]

    print(solution_1(universe))
    print(solution_2(universe))


