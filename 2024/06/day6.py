from collections import namedtuple
from enum import Enum
from typing import List

Coord = namedtuple("Coord", "x y")


class Direction(Enum):
  UP = Coord(0, -1)
  RIGHT = Coord(1, 0)
  DOWN = Coord(0, 1)
  LEFT = Coord(-1, 0)

  def next(self):
    if self == Direction.UP:
      return Direction.RIGHT
    if self == Direction.RIGHT:
      return Direction.DOWN
    if self == Direction.DOWN:
      return Direction.LEFT
    if self == Direction.LEFT:
      return Direction.UP


class Guard:
  def __init__(self, starting_position: Coord):
    self.position = starting_position
    self.direction = Direction.UP
    self.history = [starting_position]
    print(f"Starting at position {starting_position}")

  @property
  def next_position(self) -> Coord:
    return Coord(self.position.x + self.direction.value.x, self.position.y + self.direction.value.y)

  @property
  def unique_positions(self):
    return len(set(self.history))

  def rotate(self):
    self.direction = self.direction.next()
    print(f"Rotating to {self.direction.name}")

  def step(self):
    self.position = self.next_position
    self.history.append(self.position)
    print(f"Position {len(self.history)} at {self.position}")


class Map:
  obstructions: List[Coord] = []
  guard: Guard = None

  def __init__(self, grid: List[List[str]]):
    self.height = len(grid) + 1
    if self.height == 0:
      raise Exception("Invalid grid")
    self.width = len(grid[0]) + 1
    self._parse_grid(grid)

  def _parse_grid(self, grid: List[List[str]]):
    for y, row in enumerate(grid):
      for x, cell in enumerate(row):
        if cell == "#":
          self.obstructions.append(Coord(x + 1, y + 1))
        if cell == "^":
          self.guard = Guard(Coord(x + 1, y + 1))

  def step_guard(self) -> bool:
    """
    Steps guard forward by one, returns true while guard is inside map
    """
    if self.guard.next_position in self.obstructions:
      print(f"> Next position {self.guard.next_position} is obstructed")
      self.guard.rotate()

    self.guard.step()

    return self.inside_map(self.guard.next_position)

  def inside_map(self, position: Coord) -> bool:
    return 0 <= position.x < self.width and 0 <= position.y < self.height


def puzzle1(filename):
  grid = []

  with open(filename, "r") as file:
    for line in file:
      grid += [[letter for letter in line.strip()]]

  map = Map(grid)

  while map.step_guard():
    pass

  return map.guard.unique_positions
