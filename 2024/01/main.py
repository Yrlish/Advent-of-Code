from collections import Counter


def puzzle1():
    left, right = extract_lists()

    left.sort()
    right.sort()

    total = 0

    for index, item in enumerate(left):
        total += abs(item - right[index])

    print("Answer 1:", total)


def puzzle2():
    left, right = extract_lists()
    right_counter = Counter(right)
    total = 0

    for item in left:
        if item in right_counter:
            total += item * right_counter[item]

    print("Answer 2:", total)


def extract_lists():
    left = list()
    right = list()

    with open("input.txt", "r") as file:
        for line in file:
            digits = line.split("   ")
            left.append(int(digits[0]))
            right.append(int(digits[1]))

    return left, right


if __name__ == '__main__':
    puzzle1()
    puzzle2()
