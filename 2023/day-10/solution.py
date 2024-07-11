
directions = {
    (1, 0): "east",
    (-1, 0): "west",
    (0, 1): "north",
    (0, -1): "south"
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


def is_valid_move(next, current, visited, maze):

    movement = directions[(current[0] - next[0], next[1] - current[1])]
    current_symbol = maze[current[0]][current[1]]
    next_symbol = maze[next[0]][next[1]]

    valid_current, valid_next = valid_movements[movement]

    return next not in visited and current_symbol in valid_current and next_symbol in valid_next




if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Error: missing input")
        exit(1)

    filename = sys.argv[1]
    maze = get_data(filename).splitlines()

    print(maze)


