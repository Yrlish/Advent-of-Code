import unittest

import day6


class MyTestCase(unittest.TestCase):
  def test_puzzle1(self):
    self.assertEqual(41, day6.puzzle1("input_test1.txt"))
    self.assertEqual(4819, day6.puzzle1("input.txt"))


if __name__ == '__main__':
  unittest.main()
