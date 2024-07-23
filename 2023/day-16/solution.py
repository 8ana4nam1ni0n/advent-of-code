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

def paint_energized_tiles(visited: set, grid: Grid) -> None:
    energized = []
    for i in range(len(grid)):
        row = []
        for j in range(len(grid[0])):
            if (i, j) in visited:
                row.append("#")
            else:
                row.append(grid[i][j])
        energized.append(row)
    for r in energized:
        print(''.join(r))


def get_energized_tiles(grid: Grid) -> int:
    rows, cols = len(grid), len(grid[0])

    q = deque([((0, 0), DIRECTION['e'])])
    visited = {(0, 0)}

    while q:
        # print(f"Queue: {q}")
        (r, c), (dr, dc) = q.popleft()

        while (0 <= r < rows) and (0 <= c < cols):
            tile = grid[r][c]
            visited.add((r, c))
            # print(f"{(r, c)}: tile: {tile}, energized: {len(visited)}")
            # TODO: Handle case when you form a loop and infinitely repeats
            if (tile == '/') or (tile == '\\'):
                key = (tile, (dr, dc))
                dr, dc = MIRROR[key]
            elif (tile == '|') or (tile == '-'):
                directions = get_split(tile, dr, dc)
                # print(f"dir: {directions} old_dir: {(dr, dc)}")
                if directions:
                    d1, d2 = directions
                    if (r + d1[0], c + d1[1]) not in visited:
                        q.append(((r, c), d1))
                    if (r + d2[0], c + d2[1]) not in visited:
                        q.append(((r, c), d2))
                    break
            r, c = r + dr, c + dc
    paint_energized_tiles(visited, grid)
    print(visited)
    return len(visited)


if __name__ == "__main__":
    filename = 'test'

    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename) as f:
        data = f.read().splitlines()

    print(get_energized_tiles(data))
