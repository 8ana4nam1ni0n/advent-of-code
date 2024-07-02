

def get_number_by_coordinate(row: int, col: int, matrix: list[str]) -> int:
    outbound = len(matrix[row]) - 1
    start = end = col

    # check to left
    while start > 0 and matrix[row][start - 1].isdigit():
        start -= 1

    # check to right
    while end < outbound and matrix[row][end + 1].isdigit():
        end += 1

    return int(matrix[row][start:end+1])


def is_symbol(char: str) -> bool:
    return not char.isdigit() and char != '.'


def get_adjacent_coordinates(x: int, y: int, rl: int, cl: int) -> list[tuple[int, int]]:
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    adjacent = []
    for dx, dy in directions:
        zx, zy = x + dx, y + dy
        if 0 <= zx < rl and 0 <= zy < cl:
            adjacent.append((zx, zy))
    return adjacent


## part 1
def find_adjacent_numbers(matrix: list[str]) -> list[int]:
    row_len = len(matrix)
    col_len = len(matrix[0])
    adjacent_numbers = []
    for i in range(row_len):
        for j in range(col_len):
            visited_numbers = set()
            if is_symbol(matrix[i][j]):
                for x, y in get_adjacent_coordinates(i, j, row_len, col_len):
                    if matrix[x][y].isdigit():
                        visited_numbers.add(get_number_by_coordinate(x, y, matrix))
            adjacent_numbers = adjacent_numbers + list(visited_numbers)
    return adjacent_numbers

## part 2
def is_star(char: str) -> bool:
    return char == '*'

def find_gear_ratios(matrix: list[str]) -> list[int]:
    row_len = len(matrix)
    col_len = len(matrix[0])
    gears = []
    for i in range(row_len):
        for j in range(col_len):
            visited_numbers = set()
            if is_star(matrix[i][j]):
                for x, y in get_adjacent_coordinates(i, j, row_len, col_len):
                    if matrix[x][y].isdigit():
                        visited_numbers.add(get_number_by_coordinate(x, y, matrix))
            if len(visited_numbers) == 2:
                g1, g2 = list(visited_numbers)
                gear_ratio = g1 * g2
                gears.append(gear_ratio)
    return gears


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Need file input")
        exit(1)

    data_file = sys.argv[1]

    with open(data_file, "r") as f:
        data = f.read().splitlines()

    adjacent_numbers = find_adjacent_numbers(data)
    print(sum(adjacent_numbers))

    gear_ratios = find_gear_ratios(data)
    print(sum(gear_ratios))






