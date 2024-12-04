import re


def puzzle1(filename="input.txt"):
  with open(filename, "r") as file:
    memory_data = file.read()
    instructions = re.findall("mul\\((\\d{1,3}),(\\d{1,3})\\)", memory_data)
    result = 0

    for instruction in instructions:
      result += int(instruction[0]) * int(instruction[1])

    return result


def puzzle2(filename="input.txt"):
  with open(filename, "r") as file:
    memory_data = file.read()

    last_start = 0
    last_stop = memory_data.find("don't()")

    sections = [memory_data[last_start:last_stop]]

    while True:
      last_start = memory_data.find("do()", last_stop)
      last_stop = memory_data.find("don't()", last_start)

      if last_start == -1:
        break

      section = memory_data[last_start:last_stop]
      sections.append(section)

    result = 0
    for section in sections:
      for instruction in re.findall("mul\\((\\d{1,3}),(\\d{1,3})\\)", section):
        result += int(instruction[0]) * int(instruction[1])

    return result


if __name__ == '__main__':
  answer1 = puzzle1()
  print(f"Answer 1: {answer1}")
  answer2 = puzzle2()
  print(f"Answer 2: {answer2}")
  assert answer2 == 84893551
