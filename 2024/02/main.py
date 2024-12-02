import typing


def is_increasing(levels: typing.List[int]):
  return sorted(levels) == levels


def is_decreasing(levels: typing.List[int]):
  return sorted(levels, reverse=True) == levels


def check_distance(levels: typing.List[int]) -> bool:
  window_size = 2

  for index in range(len(levels) - window_size + 1):
    diff = abs(levels[index] - levels[index + 1])
    if 1 <= diff <= 3:
      continue
    else:
      return False

  return True


def puzzle1():
  total = 0

  with open("input.txt", "r") as file:
    for report in file:
      levels = report.split()
      levels = [int(level) for level in levels]

      if is_increasing(levels) or is_decreasing(levels):
        if check_distance(levels):
          total += 1

  print("Answer 1: {}".format(total))
  assert total == 670


def puzzle2():
  total = 0

  with open("input.txt", "r") as reports_file:
    for report in reports_file:
      levels = report.split()
      levels = [int(level) for level in levels]

      variants = []

      for index, level in enumerate(levels):
        variant = levels.copy()
        del variant[index]
        variants.append(variant)

      for variant in variants:
        if is_increasing(variant) or is_decreasing(variant):
          if check_distance(variant):
            total += 1
            break

  print("Answer 2: {}".format(total))
  assert total == 700


if __name__ == '__main__':
  puzzle1()
  puzzle2()
