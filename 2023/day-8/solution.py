import math


def parse_map(data: list[str]) -> dict[str, dict[str, str]]:
    return {
        d.split(' = ')[0]:{
            "L": d.split(" = ")[1].split(', ')[0][1:],
            "R": d.split(" = ")[1].split(', ')[1][:-1]
        }
        for d in data
    }

# solution 1
def traverse(instructions, map_, starting='AAA', ending=['ZZZ']) -> int:
    is_done = False
    steps = 0
    start = starting
    while not is_done:
        if map_[start][instructions[steps % len(instructions)]] in ending:
            is_done = True
        start = map_[start][instructions[steps % len(instructions)]]
        steps += 1
    return steps


def get_starting_and_ending_nodes(map_) -> tuple[list, list]:
    starting = [k for k in map_ if k.endswith('A')]
    ending = [k for k in map_ if k.endswith('Z')]
    return (starting, ending)


# solution 2
def get_lowest_common_multiplier(steps):
    return math.lcm(*steps)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Need file input")
        exit(1)

    data_file = sys.argv[1]

    with open(data_file, "r") as f:
        data = [line for line in f.read().splitlines() if line != '']

    instructions = data[0]
    map_ =  parse_map(data[1:])
    starting, ending = get_starting_and_ending_nodes(map_)

    steps = []
    for s in starting:
        steps.append(traverse(instructions, map_, starting=s, ending=ending))

    print(get_lowest_common_multiplier(steps))
