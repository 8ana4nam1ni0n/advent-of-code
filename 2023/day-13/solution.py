from typing import TypeAlias

Grid: TypeAlias = list[str]
Coordinates: TypeAlias = tuple[int, int]

def get_coordinates(grid: Grid) -> list[Coordinates]:
    return [
        (r,c)
        for r, row in enumerate(grid)
        for c, col in enumerate(row)
        if col == '#'
    ]


def get_vertical_symmetric_line(coords: list[Coordinates], grid: Grid) -> int:
    vertical = {i: [] for i in range(len(grid))}
    for r, c in coords:
        vertical[r].append(c)
    midpoints = []
    for x in vertical:
        midpoints.append(sum(vertical[x]) / len(vertical[x]))
    return round(sum(midpoints) / len(midpoints))


def get_horizontal_symmetric_line(coords: list[Coordinates], grid: Grid) -> int:
    horizontal = {i: [] for i in range(len(grid[0]))}
    for r, c in coords:
        horizontal[c].append(r)
    midpoints = []
    for x in horizontal:
        midpoints.append(sum(horizontal[x]) / len(horizontal[x]))
    return round(sum(midpoints) / len(midpoints))


def has_vertical_symmetry(symmetry_line: int, grid: Grid) -> bool:
    mid = symmetry_line
    for row in grid:
        left = len(row[0: mid+1])
        right = len(row[mid+1:])
        offset_l = 0 if left <= right else left - right
        offset_r = len(row) if right <= left else left - right
        if tuple(row[offset_l:mid+1]) != tuple(row[mid+1:offset_r][::-1]):
            return False
    return True


def has_horizontal_symmetry(symmetry_line: int, grid: Grid) -> bool:
    mid = symmetry_line
    up = len(grid[0: mid+1])
    down = len(grid[mid+1:])
    offset_u = 0 if up <= down else up - down
    offset_d = len(grid) if down <= up else up - down
    for r1, r2 in zip(grid[offset_u: mid+1], grid[mid+1: offset_d][::-1]):
        if tuple(r1) != tuple(r2):
            return False
    return True


def solution_1(grids: list[Grid]) -> int:
    result = 0
    for grid in grids:
        coords = get_coordinates(grid)
        mid_v, mid_h = get_vertical_symmetric_line(coords, grid), get_horizontal_symmetric_line(coords, grid)
        if has_vertical_symmetry(mid_v, grid):
            result += mid_v + 1 # problem uses indexing on base 1
            continue
        if has_horizontal_symmetry(mid_h, grid):
            result += 100 * (mid_h + 1)
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

