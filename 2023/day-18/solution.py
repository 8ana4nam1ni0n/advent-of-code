import sys
from dataclasses import dataclass

# TODO: Optimize solution_1 with second to eliminate
# creation of grid logic

@dataclass
class Trench:
    direction: str
    steps: int
    color: str = ''

DigPlan = list[Trench]
Grid = list[list[str]]
Boundaries = tuple[int, int, int, int]
Coordinate = tuple[int, int]

INT_TO_DIRECTION = ['R', 'D', 'L', 'U']

def get_dig_plan() -> DigPlan:
    filename = 'test'
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename) as f:
        data = [tuple(x.split()) for x in f.read().splitlines()]
    return [
        Trench(direction, int(steps), color)
        for direction, steps, color in data
    ]


def get_polygon_vertices(plan: DigPlan) -> list[Coordinate]:
    x = y = 0
    coordinates: list[Coordinate] = [(x, y)]
    for p in plan:
        match p.direction:
            case 'R':
                x += p.steps
            case 'L':
                x -= p.steps
            case 'U':
                y += p.steps
            case 'D':
                y -= p.steps
        coordinates.append((x, y))
    return coordinates


def get_perimeter(plan: DigPlan) -> int:
    return sum(p.steps for p in plan)


# Sholace algorithm implementation to calculate area of poligon but with
# a twist that includes the edges along with the fill as part of the area
def calculate_cubic_meters_of_lava(coords: list, perimeter: int) -> int:
    n = len(coords)
    area = 0
    # we use sholace to avoid doing flood fill algorithm
    for i in range(n):
        x1, y1 = coords[i]
        x2, y2 = coords[(i + 1) % n]
        area += x1 * y2
        area -= x2 * y1
    area = abs(area) / 2
    # using pick's theorem we can get the dug out interior
    B = perimeter
    I = area - B/2 + 1
    return int(I + B)

@lambda _:_()
def solution_1() -> None:
    plan = get_dig_plan()
    vertices = get_polygon_vertices(plan)
    perimeter = get_perimeter(plan)
    cubic_meters = calculate_cubic_meters_of_lava(vertices, perimeter)
    print(cubic_meters)


def parse_color(trench_plan: Trench) -> tuple[int, str]:
    color = trench_plan.color.strip('(#)')
    steps = int(color[0:5], 16)
    direction = INT_TO_DIRECTION[int(color[-1])]
    return steps, direction


@lambda _:_()
def solution_2() -> None:
    plan = [Trench(d, s) for s, d in map(parse_color, get_dig_plan()) ]
    vertices = get_polygon_vertices(plan)
    perimeter = get_perimeter(plan)
    cubic_meters = calculate_cubic_meters_of_lava(vertices, perimeter)
    print(cubic_meters)
