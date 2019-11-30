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
        pass


if __name__ == '__main__':
    unittest.main()