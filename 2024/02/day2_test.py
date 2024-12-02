import unittest

import day2


class Day2Test(unittest.TestCase):
  def test_puzzle1(self):
    answer = day2.puzzle1("input_test.txt")
    self.assertEqual(answer, 2, "Example has the answer 2")

  def test_puzzle2(self):
    answer = day2.puzzle2("input_test.txt")
    self.assertEqual(answer, 4, "Example has the answer 4")


if __name__ == '__main__':
  unittest.main()
