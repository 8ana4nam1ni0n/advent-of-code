import sys
from dataclasses import dataclass


@dataclass
class Trench:
    direction: str
    steps: int
    color: str

DigPlan = list[Trench]
Grid = list[str]


def get_dig_plan() -> DigPlan:
    filename = 'test'
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename) as f:
        data = [tuple(x.split()) for x in f.read().splitlines()]
    return [Trench(direction, int(steps), color) for direction, steps, color in data]


def detect_grid_dimensions(plan: DigPlan) -> tuple[int, int]:
    horizontal_movement = filter(lambda x: x.direction in ['R', 'L'], plan)
    width = 0
    curr_w = 0
    for step in horizontal_movement:
        curr_w += step.steps if step.direction == 'R' else -step.steps
        width = max(abs(curr_w), width)
    vertical_movement = filter(lambda x: x.direction in ['U', 'D'], plan)
    height = 0
    curr_h = 0
    for step in vertical_movement:
        curr_h += step.steps if step.direction == 'D' else -step.steps
        height = max(abs(curr_h), height)
    return width + 1, height + 1


@lambda _:_()
def solution_1() -> None:
    plan = get_dig_plan()
    w, h = detect_grid_dimensions(plan)
    print(f'dimensions detected: w: {w}, h: {h}')
    grid = [[0]*w]*h
    print(grid)

