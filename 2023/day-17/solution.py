import sys
from heapq import heappop, heappush
from typing import TypeAlias

Grid: TypeAlias = list[list[int]]
Heap: TypeAlias = list[tuple[int, int, int, int, int, int]]

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def is_valid(row: int, col: int, grid: Grid) -> bool:
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def push_to_heap(heap: Heap, row: int, col: int, drow: int, dcol: int, move: int, heatloss: int, grid: Grid) -> None:
    next_row = row + drow
    next_col = col + dcol
    if is_valid(next_row, next_col, grid):
        heappush(heap, (heatloss + grid[next_row][next_col], next_row, next_col, drow, dcol, move))


# Djikstra
def get_minimum_heat_path(grid: Grid, at_most=3, at_min=1) -> int:
    heap: Heap = [(0, 0, 0, 0, 0, 0)]
    visited = set()
    min_heat_loss = -1

    while heap:
        heatloss, r, c, dr, dc, move = heappop(heap)
        hash_ = (r, c, dr, dc, move)

        # check if we reached end
        if r == len(grid) - 1 and c == len(grid[0]) - 1 and move >= at_min:
            min_heat_loss = heatloss
            break

        if hash_ in visited:
            continue

        visited.add(hash_)

        if move < at_most and (dr, dc) != (0, 0):
            push_to_heap(heap, r, c, dr, dc, move + 1, heatloss, grid)

        if move >= at_min or (dr, dc) == (0, 0):
            for ndr, ndc in DIRECTIONS:
                if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                    push_to_heap(heap, r, c, ndr, ndc, 1, heatloss, grid)

    return min_heat_loss


def solution_1(grid: Grid) -> None:
    print(get_minimum_heat_path(grid))


def solution_2(grid: Grid) -> None:
    print(get_minimum_heat_path(grid, at_most=10, at_min=4))


if __name__ == "__main__":

    filename = 'test'
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename) as f:
        grid = [list(map(int, line)) for line in f.read().splitlines()]

    solution_1(grid)
    solution_2(grid)
