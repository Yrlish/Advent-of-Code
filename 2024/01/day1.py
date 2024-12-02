from collections import Counter


def puzzle1(filename="input.txt") -> int:
  left, right = extract_lists(filename)

  left.sort()
  right.sort()

  total = 0

  for index, item in enumerate(left):
    total += abs(item - right[index])

  return total


def puzzle2(filename="input.txt"):
  left, right = extract_lists(filename)
  right_counter = Counter(right)
  total = 0

  for item in left:
    if item in right_counter:
      total += item * right_counter[item]

  return total


def extract_lists(filename: str):
  left = list()
  right = list()

  with open(filename, "r") as file:
    for line in file:
      digits = line.split("   ")
      left.append(int(digits[0]))
      right.append(int(digits[1]))

  return left, right


if __name__ == '__main__':
  answer1 = puzzle1()
  print(f"Answer 1: {answer1}")

  answer2 = puzzle2()
  print(f"Answer 2: {answer2}")
