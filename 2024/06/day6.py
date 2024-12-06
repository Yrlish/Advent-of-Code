from collections import namedtuple
from enum import Enum
from typing import List, Set

Coord = namedtuple("Coord", "x y")


class DupeExcetion(Exception):
  pass


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
    self.path = {starting_position}
    self.cache = {(starting_position, Direction.UP)}
    # print(f"Starting at position {starting_position}")

  @property
  def next_position(self) -> Coord:
    return Coord(self.position.x + self.direction.value.x, self.position.y + self.direction.value.y)

  @property
  def unique_positions(self):
    return len(set(self.path))

  def rotate(self):
    self.direction = self.direction.next()
    # print(f"Rotating to {self.direction.name}")

  def step(self):
    self.position = self.next_position
    self.path.add(self.position)

    cache_item = (self.position, self.direction)
    if not cache_item in self.cache:
      self.cache.add(cache_item)
    else:
      raise DupeExcetion()
    # print(f"Position {len(self.history)} at {self.position}")

  def same_path(self, position: Coord) -> bool:
    return (position, self.direction) in self.cache


class Map:
  def __init__(self, grid: List[List[str]]):
    self.height = len(grid)
    if self.height == 0:
      raise Exception("Invalid grid")
    self.width = len(grid[0])
    self.obstructions: Set[Coord] = set()
    self.guard: Guard = None

    self._parse_grid(grid)

  def _parse_grid(self, grid: List[List[str]]):
    for y, row in enumerate(grid):
      for x, cell in enumerate(row):
        if cell == "#":
          self.obstructions.add(Coord(x, y))
        if cell == "^":
          self.guard = Guard(Coord(x, y))

  def step_guard(self) -> bool:
    if self.guard.next_position in self.obstructions:
      # print(f"> Next position {self.guard.next_position} is obstructed")
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


def puzzle2(filename):
  grid = []

  with open(filename, "r") as file:
    for line in file:
      grid += [[letter for letter in line.strip()]]

  map = Map(grid)

  while map.step_guard():
    pass

  candidates = list(map.guard.path)[1:]
  loops = 0
  print(f"Candidates: {len(candidates)}")

  for i, candidate in enumerate(candidates, 1):
    map2 = Map(grid)
    map2.obstructions.add(candidate)

    try:
      while map2.step_guard():
        pass
    except DupeExcetion:
      loops += 1
      continue

    if (i % 100) == 0:
      print(f"Candidate #{i} of {len(candidates)} - loops: {loops}")

  return loops
