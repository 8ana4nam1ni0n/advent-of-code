import operator
import re
import sys
from collections import deque

OPS = {
    '<': operator.lt,
    '>': operator.gt
}

Workflows = dict[str, tuple[str,...]]
Ratings = list[dict[str, int]]


def get_data() -> tuple[str, str]:
    filename = 'test'
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    with open(filename) as f:
        workflows, ratings = f.read().split('\n\n')
    return workflows, ratings


def parse_workflows(raw_workflows: str) -> Workflows:
    workflows = {}
    for workflow in raw_workflows.split():
        name, rules = workflow.strip('}').split('{')
        rules = rules.split(',')
        workflows[name] = tuple(rules)
    return workflows


def parse_ratings(raw_ratings: str) -> Ratings:
    ratings = []
    for rating in raw_ratings.strip('{}').split():
        ratings.append({k: int(v) for k, v in re.findall(r'(\w)=(\d+)', rating)})
    return ratings


def process_condition(condition: str, rating: dict[str,int]) -> bool:
    if not ('<' in condition or '>' in condition):
        return True
    identifier, ops, number = re.findall(r'(\w)(<|>)(\d+)', condition).pop()
    return OPS[ops](rating[identifier], int(number))


def process_workflow(rules: tuple[str,...], rating: dict[str, int]) -> str:
    for rule in rules:
        if ':' in rule:
            condition, result = rule.split(':')
            if process_condition(condition, rating):
                return result
        else:
            return rule
    return ''


def process_rating(workflows: Workflows, rating: dict[str, int]) -> str:
    current_workflow: str = 'in'
    while current_workflow not in ('A', 'R'):
        current_workflow = process_workflow(workflows[current_workflow], rating)
    return current_workflow


@lambda _:_()
def solution_1() -> None:
    raw_workflows, raw_ratings = get_data()
    workflows = parse_workflows(raw_workflows)
    ratings = parse_ratings(raw_ratings)
    accepted = [rating for rating in ratings if process_rating(workflows, rating) == 'A']
    result = sum(sum(rating.values()) for rating in accepted)
    print(result)


def calculate_combinations(combinations):
    result = 1
    for low, high in combinations.values():
        result *= (high - low + 1)
    return result


# TODO: Clean code  a bit
def count_accepted_combinations(workflows: Workflows) -> int:
    accepted = 0
    xmas_combinations = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}
    queue = deque([('in', xmas_combinations)])

    while queue:
        workflow, curr_combination = queue.popleft()

        match workflow:
            case 'A':
                accepted += calculate_combinations(curr_combination)
                continue
            case 'R':
                continue

        for rule in workflows[workflow]:
            if ':' not in rule:
                queue.append((rule, curr_combination))
                continue
            condition, next_workflow = rule.split(':')
            part, operation, number = condition[0], condition[1], int(condition[2:])
            low, high = curr_combination[part]

            if operation == '<':
                true_comb, false_comb = (low, min(number - 1, high)), (max(number, low), high)
            else:
                true_comb, false_comb = (max(number + 1, low), high), (low, min(number, high))

            if true_comb[0] <= true_comb[1]:
                new_combinations = curr_combination.copy()
                new_combinations[part] = true_comb
                queue.append((next_workflow, new_combinations))

            if false_comb[0] <= false_comb[1]:
                curr_combination[part] = false_comb

    return accepted



@lambda _:_()
def solution_2() -> None:
    raw_workflows, _ = get_data()
    workflows = parse_workflows(raw_workflows)
    print(count_accepted_combinations(workflows))



