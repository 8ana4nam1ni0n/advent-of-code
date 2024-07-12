from collections import deque

coord_to_cardinal_point = {
    (0, 1): "east",
    (0, -1): "west",
    (-1, 0): "north",
    (1, 0): "south"
}


path = {
    '|': ('north', 'south'),
    '-': ('east', 'west'),
    'L': ('north', 'east'),
    'J': ('north', 'west'),
    '7': ('south', 'west'),
    'F': ('south', 'east'),
    '.': ()
}

valid_movements = {
    "east": ({"S", "-" , "F" , "L"},{ "7" , "J" , "-"}),
    "west": ({"S", "-" , "7" , "J"},{ "L" , "F" , "-"}),
    "north": ({"S", "|", "L" , "J"},{ "7" , "F" , "|"}),
    "south": ({"S", "|" , "F" , "7"},{ "J" , "L" , "|"})
}

def get_data(filename: str) -> str:
    with open(filename, 'r') as f:
        return f.read()


def is_valid_move(nexxt, current, visited, maze):

    if nexxt[0] < 0 or nexxt[1] < 0 or nexxt[0] >= len(maze) or nexxt[1] >= len(maze[0]):
        return False

    movement = coord_to_cardinal_point[(nexxt[0] - current[0], nexxt[1] - current[1])]
    current_symbol = maze[current[0]][current[1]]
    next_symbol = maze[nexxt[0]][nexxt[1]]

    valid_current, valid_next = valid_movements[movement]

    return nexxt not in visited and current_symbol in valid_current and next_symbol in valid_next


def get_starting_point(maze: list[str]) -> tuple[int, int]:
    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if 'S' in col:
                return (i, j)
    return (0, 0)


def solution_1(start: tuple[int, int], maze: list[str]) -> int:
    queue = deque([(start, 0)])
    max_steps = 0
    visited = set([start])

    while queue:
        (y, x), steps = queue.popleft()

        max_steps = max(steps, max_steps)

        for (dy, dx) in coord_to_cardinal_point:
            nexxt = y + dy, x + dx
            current = y, x
            if is_valid_move(nexxt, current, visited, maze):
                visited.add(nexxt)
                queue.append((nexxt, steps + 1))

    return max_steps


def print_maze(maze):
    rows, cols = len(maze), len(maze[0])
    for row in range(rows):
        if row == 0:
            print(f" : {' '.join(map(str, range(cols)))}")
        print(f"{row}: {' '.join(maze[row])}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Error: missing input")
        exit(1)

    filename = sys.argv[1]
    maze = get_data(filename).splitlines()

    start = get_starting_point(maze)

    print(solution_1(start, maze))
