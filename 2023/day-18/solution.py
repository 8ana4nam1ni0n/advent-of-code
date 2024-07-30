import sys
from collections import deque
from dataclasses import dataclass

# TODO: Optimize solution_1 with second to eliminate
# creation of grid logic

@dataclass
class Trench:
    direction: str
    steps: int
    color: str = ''


DIRECTION = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
}


INT_TO_DIRECTION = ['R', 'D', 'L', 'U']


DigPlan = list[Trench]
Grid = list[list[str]]
Boundaries = tuple[int, int, int, int]
Dimensions = tuple[int, int]
Coordinates = list[Dimensions]


def get_dig_plan() -> DigPlan:
    filename = 'test'
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename) as f:
        data = [tuple(x.split()) for x in f.read().splitlines()]
    return [Trench(direction, int(steps), color) for direction, steps, color in data]


def calculate_terrain_boundaries(plan: DigPlan) -> Boundaries:
    x, y = 0, 0
    min_x, min_y = 0, 0
    max_x, max_y = 0, 0
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
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        min_x = min(min_x, x)
        min_y = min(min_y, y)
    return max_x, min_x, max_y, min_y


def dig_trench(terrain: Grid, plan: DigPlan, boundaries: Boundaries) -> Grid:
    mx_x, mn_x, mx_y, mn_y = boundaries
    x, y = -mn_x, -mn_y
    for trench in plan:
        dx, dy = DIRECTION[trench.direction]
        for _ in range(trench.steps):
            x += dx
            y += dy
            terrain[y][x] = '#'
    return terrain[::-1]


def detect_grid_dimensions(boundaries: Boundaries) -> Dimensions:
    max_x, min_x, max_y, min_y = boundaries
    return max_x - min_x + 1, max_y - min_y + 1


def make_grid(width: int, height: int) -> Grid:
    return [['.' for _ in range(width)] for _ in range(height)]


def is_valid_move(coord: tuple[int, int] , visited: list, grid: Grid) -> bool:
    y, x = coord
    if (x < 0 or x >= len(grid[0])) or (y < 0 or y >= len(grid)):
        return False
    is_correct_symbol = (grid[y][x] == '#')
    is_not_visited = coord not in visited
    return is_correct_symbol and is_not_visited



def get_edges_coordinates(terrain: Grid) -> list:
    start = 0, terrain[0].index('#')
    queue = deque([start])
    # we used a list instead of a set because we need to guarantee the order
    # for sholace algorithm to work (since nodes need to be connected)
    visited = [start]
    while queue:
        y, x = queue.popleft()
        for dy, dx in DIRECTION.values():
            nexxt = y + dy, x + dx
            if is_valid_move(nexxt, visited, terrain):
                visited.append(nexxt)
                queue.append(nexxt)
                break
    return visited


def calculate_cubic_meters_of_lava(coords: list, boundary_points=None) -> int:
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
    B = n if not boundary_points else boundary_points
    i = area - B/2 + 1
    return int(i + B)

@lambda _:_()
def solution_1() -> None:
    plan = get_dig_plan()
    edges = calculate_terrain_boundaries(plan)
    w, h = detect_grid_dimensions(edges)
    grid = make_grid(w, h)
    grid = dig_trench(grid, plan, edges)
    coords = get_edges_coordinates(grid)
    cubic_meters = calculate_cubic_meters_of_lava(coords)
    print(cubic_meters)


def parse_color(trench_plan: Trench) -> tuple[int, str]:
    color = trench_plan.color.strip('(#)')
    return int(color[0:5],16), INT_TO_DIRECTION[int(color[-1])]

def get_polygon_vertices(plan: DigPlan) -> list[tuple[int, int]]:
    x, y = 0, 0
    coordinates = [(x, y)]
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

@lambda _:_()
def solution_2() -> None:
    old_plan = get_dig_plan()
    new_plan = [Trench(d, s) for s, d in map(parse_color, old_plan) ]
    vertices = get_polygon_vertices(new_plan)
    perimeter = get_perimeter(new_plan)
    cubic_meters = calculate_cubic_meters_of_lava(vertices, boundary_points=perimeter)
    print(cubic_meters)
