import concurrent.futures
import sys
from collections import deque
from typing import TypeAlias

Grid: TypeAlias = list[str]


DIRECTION = {
    'n': (-1, 0),
    's': ( 1, 0),
    'e': ( 0, 1),
    'w': ( 0,-1)
}


MIRROR = {
    ('\\', DIRECTION['e']): DIRECTION['s'],
    ('\\', DIRECTION['w']): DIRECTION['n'],
    ('\\', DIRECTION['n']): DIRECTION['w'],
    ('\\', DIRECTION['s']): DIRECTION['e'],
    ('/', DIRECTION['e']): DIRECTION['n'],
    ('/', DIRECTION['w']): DIRECTION['s'],
    ('/', DIRECTION['n']): DIRECTION['e'],
    ('/', DIRECTION['s']): DIRECTION['w'],
}


def get_split(tile: str, row, col) -> tuple[tuple[int, int], tuple[int, int]] | None:
    old_direction = (row, col)

    if (tile == '|') and (old_direction == DIRECTION['e'] or old_direction == DIRECTION['w']):
        return DIRECTION['n'], DIRECTION['s']
    if (tile == '-') and (old_direction == DIRECTION['n'] or old_direction == DIRECTION['s']):
        return DIRECTION['e'], DIRECTION['w']
    return None


def get_energized_tiles(grid: Grid, sr: int, sc: int, direction: tuple[int, int]) -> int:
    rows, cols = len(grid), len(grid[0])
    q = deque([((sr, sc), direction)])
    visited = set()

    while q:
        (r, c), (dr, dc) = q.popleft()

        while (0 <= r < rows) and (0 <= c < cols):
            tile = grid[r][c]
            if (tile == '/') or (tile == '\\'):
                key: tuple[str, tuple[int, int]] = (tile, (dr, dc))
                dr, dc = MIRROR[key]
                if ((r, c), (dr, dc)) in visited:
                    break
            elif (tile == '|') or (tile == '-'):
                directions = get_split(tile, dr, dc)
                if directions:
                    d1, d2 = directions
                    # check going up or east depending on the tile
                    if ((r, c), d1) not in visited:
                        visited.add(((r, c), d1))
                        q.append(((r, c), d1))
                    # check going down or west depending on the tile
                    if ((r, c), d2) not in visited:
                        visited.add(((r, c), d2))
                        q.append(((r, c), d2))
                    break
            visited.add(((r, c), (dr, dc)))
            r, c = r + dr, c + dc
    # set the set for only r and c to avoid double counting
    # the tiles that were crossed by multiple paths
    return len({(r, c) for ((r, c), _) in visited})


def get_edges(grid: Grid) -> tuple[list[tuple[int, int]], ...]:
    rows, cols = len(grid), len(grid[0])

    TOP = [(0, i) for i in range(cols)]
    LEFT = [(i, 0) for i in range(rows)]
    RIGHT = [(i, cols-1) for i in range(rows)]
    BOTTOM = [(rows-1, i) for i in range(cols)]

    return TOP, LEFT, RIGHT, BOTTOM



def solution_1(grid: Grid) -> None:
    energized = get_energized_tiles(grid, 0, 0, DIRECTION['e'])
    print(energized)


def run_get_energized_tiles(args):
    return get_energized_tiles(*args)

def run_jobs(grid: Grid, edge, direction: str) -> int:
    result = []
    args = [(grid, r, c, DIRECTION[direction]) for r, c in edge]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        result = max(executor.map(run_get_energized_tiles, args))
    return result


def solution_2(grid: Grid) -> None:
    energized = []
    top, left, right, bottom = get_edges(grid)
    # by running things in parallel you speed up the thing by 2 seconds smh
    # yep I wasted my time lol
    for edge, direction in [(top, 's'), (left, 'e'), (right, 'w'), (bottom, 'n')]:
        energized.append(run_jobs(grid, edge, direction))
    print(max(energized))


if __name__ == "__main__":
    filename = 'test'

    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename) as f:
        data = f.read().splitlines()

    solution_1(data)
    solution_2(data)
