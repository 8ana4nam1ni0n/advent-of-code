import operator
import re
import sys

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



