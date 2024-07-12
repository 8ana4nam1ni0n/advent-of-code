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


# An optimization for this could be just calculate the path of the loop
# and divide the number of visited nodes by 2 since the farthest point will always
# be in the middle of the loop
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


# Solution 2
def get_nodes_in_loop(start: tuple[int, int], maze: list[str]) -> list[tuple[int, int]]:
    queue = deque([start])
    visited = [start]

    while queue:
        y, x = queue.popleft()

        for dy, dx in coord_to_cardinal_point:
            nexxt = y + dy, x + dx
            current = y, x
            if is_valid_move(nexxt, current, visited, maze):
                visited.append(nexxt)
                queue.append(nexxt)
                # we break since we dont need to path find we need all nodes
                # to be connected for the sholace algorithm to work
                break

    return visited


def sholace(coordinates) -> float:
    n = len(coordinates)
    area = 0

    for i in range(n):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[(i + 1) % n]
        area += x1 * y2
        area -= x2 * y1

    return abs(area) / 2


# this is picks theorem
def get_tiles_within_loop(coordinates):
    area = sholace(coordinates)
    b = len(coordinates)
    i = area - b/2 + 1
    return i


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

    nodes = get_nodes_in_loop(start, maze)
    print(get_tiles_within_loop(nodes))
