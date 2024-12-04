from collections import namedtuple
from typing import List

# x, y
directions_straight = [
  [1, 0],  # right
  [-1, 0],  # left
  [0, 1],  # up
  [0, -1],  # down
]
directions_diagonal = [
  [1, 1],  # up-right
  [1, -1],  # down-right
  [-1, 1],  # up-left
  [-1, -1],  # down-left
]
all_directions = directions_straight + directions_diagonal

Coord = namedtuple("Coord", "x y")


def build_grid(filename):
  grid = []

  with open(filename, "r") as file:
    for line in file:
      grid += [[letter for letter in line.strip()]]

  return grid


def is_inside_grid(grid, coord: Coord) -> bool:
  return 0 <= coord.x < len(grid[0]) and 0 <= coord.y < len(grid)


def check_xmas(grid: List[List[str]], x: int, y: int):
  matches = 0

  for [dx, dy] in all_directions:
    letters = []
    coord = Coord(x, y)

    for _ in range(4):
      if not is_inside_grid(grid, coord):
        break

      letters.append(grid[coord.y][coord.x])
      coord = Coord(coord.x + dx, coord.y + dy)

    if letters == list("XMAS") or letters == list("XMAS")[::-1]:
      matches += 1

  return matches


def check_x_mas(grid: List[List[str]], x: int, y: int):
  letters = []
  coord = Coord(x, y)

  for [dx, dy] in directions_diagonal:
    new_coord = Coord(coord.x + dx, coord.y + dy)

    if not is_inside_grid(grid, new_coord):
      break

    letters.append(grid[new_coord.y][new_coord.x])

  return (
      len(letters) == 4
      and letters.count("M") == 2
      and letters.count("S") == 2
      and letters[0] != letters[3]
  )


def puzzle1(filename="input.txt"):
  grid = build_grid(filename)
  return sum([check_xmas(grid, x, y) for y, row in enumerate(grid) for x, cell in enumerate(row) if cell == "X"])


def puzzle2(filename="input.txt"):
  grid = build_grid(filename)
  return sum([1 for y, row in enumerate(grid) for x, cell in enumerate(row) if cell == "A" and check_x_mas(grid, x, y)])


if __name__ == '__main__':
  answer1 = puzzle1()
  print(f"Answer 1: {answer1}")

  answer2 = puzzle2()
  print(f"Answer 2: {answer2}")
