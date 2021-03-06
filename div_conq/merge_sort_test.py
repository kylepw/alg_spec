from random import randint, seed
import unittest
from merge_sort import msort


class TestMsort(unittest.TestCase):
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
            self.assertEqual(msort(arg), expected)

    def test_msort(self):
        data = self.gen_data(8)
        for d in data:
            msort(d)
            self.assertEqual(d, sorted(d))


if __name__ == '__main__':
    unittest.main()