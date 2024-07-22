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

    if (tile == '|') and (old_direction == DIRECTION['e']) or (old_direction == DIRECTION['w']):
        return DIRECTION['n'], DIRECTION['s']
    if (tile == '-') and (old_direction == DIRECTION['n']) or (old_direction == DIRECTION['s']):
        return DIRECTION['e'], DIRECTION['w']
    return None


def get_energized_tiles(grid: Grid) -> int:
    rows, cols = len(grid), len(grid[0])
    tiles = 1

    q = deque([((0, 0), DIRECTION['e'])])

    while q:
        print(f"Queue: {q}")
        (r, c), (dr, dc) = q.popleft()
        nr, nc = r + dr, c + dc

        # TODO need to mark nodes tiles as visited to prevent infinite loops
        while (0 <= nr < rows) and (0 <= nc < cols):
            tile = grid[nr][nc]
            tiles += 1
            print(f"{(r, c)}: tile: {tile}, energized: {tiles}")
            if (tile == '/') or (tile == '\\'):
                key = (tile, (dr, dc))
                dr, dc = MIRROR[key]
            elif (tile == '|') or (tile == '-'):
                directions = get_split(tile, dr, dc)
                if directions:
                    d1, d2 = directions
                    q.append(((nr, nc), d1))
                    q.append(((nr, nc), d2))
                    break
            nr, nc = nr + dr, nc + dc
    return tiles


if __name__ == "__main__":
    filename = 'test'

    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename) as f:
        data = f.read().splitlines()

    print(get_energized_tiles(data))
