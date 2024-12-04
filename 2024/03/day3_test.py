import unittest

import day3


class Day3Test(unittest.TestCase):
  def test_puzzle1(self):
    self.assertEqual(day3.puzzle1("input_test1.txt"), 161)

  def test_puzzle2(self):
    self.assertEqual(day3.puzzle2("input_test2.txt"), 48)


if __name__ == '__main__':
  unittest.main()
