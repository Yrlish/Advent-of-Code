import unittest

import day6


class MyTestCase(unittest.TestCase):
  def test_puzzle1(self):
    self.assertEqual(day6.puzzle1("input_test1.txt"), 41)
    self.assertEqual(day6.puzzle1("input.txt"), 4819)

  def test_puzzle2(self):
    self.assertEqual(day6.puzzle2("input_test1.txt"), 6)

    answer = day6.puzzle2("input.txt")
    print(f"> Answer 2: {answer}")
    self.assertGreater(answer, 1779)
    self.assertEqual(answer, "NOT SOLVED")


if __name__ == '__main__':
  unittest.main()
