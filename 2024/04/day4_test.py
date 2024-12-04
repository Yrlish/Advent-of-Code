import unittest

import day4


class Day4Test(unittest.TestCase):
  def test_puzzle1(self):
    self.assertEqual(day4.puzzle1("input_test1_2.txt"), 18)
    self.assertEqual(day4.puzzle1("input.txt"), 2378)

  def test_puzzle2(self):
    self.assertEqual(day4.puzzle2("input_test2.txt"), 9)
    self.assertEqual(day4.puzzle2("input.txt"), 1796)


if __name__ == '__main__':
  unittest.main()
