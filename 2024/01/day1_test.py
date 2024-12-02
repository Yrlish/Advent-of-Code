import unittest

import day1


class Day1Test(unittest.TestCase):
  def test_puzzle1(self):
    answer = day1.puzzle1("input_test1.txt")
    self.assertEqual(answer, 11, "Example has the answer 11")

  def test_puzzle2(self):
    answer = day1.puzzle2("input_test2.txt")
    self.assertEqual(answer, 31, "Example has the answer 31")


if __name__ == '__main__':
  unittest.main()
