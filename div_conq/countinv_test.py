from countinv import count_inversions
import unittest


class TestCountInv(unittest.TestCase):
    def setUp(self):
        pass

    def test_bad_values(self):
        self.assertEqual(count_inversions('str'), (None, None))
        self.assertEqual(count_inversions(101), (None, None))
        self.assertEqual(count_inversions(['str', 1]), (None, None))

    def test_base_cases(self):
        self.assertEqual(count_inversions([]), ([], 0))
        self.assertEqual(count_inversions([101]), ([101], 0))

    def test_sorted_arrays(self):
        self.assertEqual(count_inversions([1, 2, 3, 999]), ([1, 2, 3, 999], 0))
        self.assertEqual(count_inversions([-22, 10, 45, 999, 2001]), ([-22, 10, 45, 999, 2001], 0))

    def test_unsorted_arrays(self):
        self.assertEqual(count_inversions([1, 3, 5, 2, 4, 6]), ([1, 2, 3, 4, 5, 6], 3))
        self.assertEqual(count_inversions([9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0]), ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 56))
        self.assertEqual(count_inversions([37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45]), ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], 590))




if __name__ == '__main__':
    unittest.main()