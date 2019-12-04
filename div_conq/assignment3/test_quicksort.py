from random import randint, seed
import unittest
from quicksort import qsort, _left_pivot, _right_pivot, _mid_pivot


class TestQuickSort(unittest.TestCase):
    def gen_data(self, n):
        """Return list of n-lists of 1 through n -1 random integers."""
        data = []
        for x in range(1, n):
            seed(x)
            d = []
            for _ in range(x):
                d.append(randint(-100, 999))
            data.append(d)
        return data

    def test_bad_values(self):
        bad_data = (
            (None, None),
            (1, None),
            ('abc', None)
        )
        for arg, expected in bad_data:
            with self.assertRaises(ValueError):
                self.assertEqual(qsort(arg), expected)

    def test_valid_values_with_default_rand_pivot(self):
        data = self.gen_data(8)
        for d in data:
            qsort(d)
            self.assertEqual(d, sorted(d))

    def test_valid_values_with_left_pivot(self):
        data = self.gen_data(8)
        for d in data:
            qsort(d, choose_pivot=_left_pivot)
            self.assertEqual(d, sorted(d))

    def test_valid_values_with_right_pivot(self):
        data = self.gen_data(8)
        for d in data:
            qsort(d, choose_pivot=_right_pivot)
            self.assertEqual(d, sorted(d))

    def test_valid_values_with_mid_pivot(self):
        data = self.gen_data(8)
        for d in data:
            qsort(d, choose_pivot=_mid_pivot)
            self.assertEqual(d, sorted(d))


if __name__ == '__main__':
    unittest.main()