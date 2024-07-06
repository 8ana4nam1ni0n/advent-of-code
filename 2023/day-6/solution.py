import math
import operator
from functools import reduce


def calculate_possible_wins(time, distance):
    determinant = math.sqrt(time ** 2 - 4 * distance)
    n1 = math.ceil((time - determinant) / 2)
    n2 = math.floor((time + determinant) / 2)

    is_inclusive = n1 * n2 > distance

    solutions = n2 - n1 + 1 if is_inclusive else n2 - n1 - 1

    return solutions


# part 1 solution
def get_possible_wins(times, distances):
    # we use quadratic formula for this
    possible_wins = []
    for t, d in zip(times, distances):
       possible_wins.append(calculate_possible_wins(t, d))
    return reduce(operator.mul, possible_wins)

# part 2 solution
def number_list_to_int(number_list):
    return int(''.join(map(str, number_list)))

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Missing Input")
        exit(1)

    filename = sys.argv[1]

    with open(filename, "r") as  f:
        data = [list(map(int, d.split(':')[1].strip().split())) for d in  f.read().splitlines()]

    times, distances = data
    print(get_possible_wins(times, distances))

    fixed_time = number_list_to_int(times)
    fixed_distance = number_list_to_int(distances)
    print(calculate_possible_wins(fixed_time, fixed_distance))

