import unittest

import day5


class Day5Test(unittest.TestCase):
  def test_puzzle1(self):
    self.assertEqual(143, day5.puzzle1("input_test1.txt"), "Example answer should be 143")
    self.assertEqual(5651, day5.puzzle1("input.txt"))

  def test_puzzle2(self):
    self.assertEqual(123, day5.puzzle2("input_test1.txt"), "Example answer should be 123")

    actual = day5.puzzle2("input.txt")
    print(actual)

    self.assertGreater(actual, 4512)
    self.assertLess(actual, 10944)
    self.assertNotEqual(actual, 10394)
    self.assertEqual(actual, 4743)

if __name__ == '__main__':
  unittest.main()
