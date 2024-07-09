


def process_sequence(seq: list[int]) -> int:

    if all(x == seq[0] for x in seq):
        return seq[-1]

    return seq[-1] + process_sequence([seq[i+1] - s for i, s in enumerate(seq[:-1])])

def solution_1(data: list[list[int]]) -> int:
    total = 0
    for seq in data:
        total += process_sequence(seq)
    return total


def process_sequence_2(seq: list[int]) -> int:

    if all(x == 0 for x in seq):
        return seq[0]

    return seq[0] - process_sequence_2([seq[i+1] - s for i, s in enumerate(seq[:-1])])

def solution_2(data: list[list[int]]) -> int:
    total = 0
    for seq in data:
        total += process_sequence_2(seq)
    return total



if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Error: missing input")
        exit(1)

    filename = sys.argv[1]

    with open(filename, 'r') as f:
        data = [list(map(int, line.split())) for line in f.read().splitlines()]

    print(solution_1(data))
    print(solution_2(data))
