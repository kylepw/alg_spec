import unittest
from mm import get_medians


class TestGetMedians(unittest.TestCase):
    def test_even(self):
        nums = [6, 3, 4, 5, 1, 2]
        self.assertEqual(get_medians(nums), [6, 3, 4, 4, 4, 3])

    def test_odd(self):
        nums = [6, 3, 4, 5, 1]
        self.assertEqual(get_medians(nums), [6, 3, 4, 4, 4])


if __name__ == '__main__':
    unittest.main()
