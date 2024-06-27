import re


def get_file_data():
    with open("input.txt", "r") as input_file:
        data = input_file.readlines()
    return data

#### SOLUTION PART 1
def get_calibration_values(data: list[str]):
    return sum(get_calibration_value(d) for d in data)

def get_calibration_value(data: str):
    left, right = 0, len(data) - 1
    found_left, found_right = False, False
    for _ in data:
        if data[left].isnumeric():
            found_left = True
        else:
            left += 1

        if data[right].isnumeric():
            found_right = True
        else:
            right -= 1


        if found_left and found_right:
            return int(data[left] + data[right])

    return 0

#### SOLUTION PART 2
lookahead = re.compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))')

def word_to_number(word: str) -> str:
    return {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }.get(word, word)

def get_calibration_value_corrected(data: str) -> int:
    first = last = ''
    matches = re.findall(lookahead, data)
    if len(matches) == 1:
        first = last = matches[0]
    elif len(matches) == 2:
        first, last = matches
    else:
        first, *_, last = matches

    first = word_to_number(first)
    last = word_to_number(last)
    return int(first+last)


def solution2(data: list[str]) -> int:
    return sum(get_calibration_value_corrected(d) for d in data)

data = get_file_data()
print("======== Part 1: solution ========")
print(get_calibration_values(data))

print("======== Part 2: solution ========")
# data = [
#     'two1nine',
#     'eightwothree',
#     'abcone2threexyz',
#     'xtwone3four',
#     '4nineeightseven2',
#     'zoneight234',
#     '7pqrstsixteen'
# ]

print(solution2(data))
