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


def get_energized_tiles(grid: Grid, sr=0, sc=0, delta=DIRECTION['e']) -> int:
    rows, cols = len(grid), len(grid[0])
    q = deque([((sr, sc), delta)])
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
                    if (r + d1[0], c + d1[1]) not in visited:
                        visited.add(((r, c), (d1[0], d1[1])))
                        q.append(((r, c), d1))
                    if (r + d2[0], c + d2[1]) not in visited:
                        visited.add(((r, c), (d2[0], d2[1])))
                        q.append(((r, c), d2))
                    break

            visited.add(((r, c), (dr, dc)))
            r, c = r + dr, c + dc
    return len({(r, c) for ((r, c), _) in visited})


def solution_1(grid: Grid) -> None:
    energized = get_energized_tiles(grid)
    print(energized)


def solution_2(grid: Grid) -> None:
    energized = 0
    print(energized)

if __name__ == "__main__":
    filename = 'test'

    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename) as f:
        data = f.read().splitlines()

    solution_1(data)
    solution_2(data)
