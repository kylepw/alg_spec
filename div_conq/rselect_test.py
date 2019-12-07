from random import randrange
from rselect import rs
import unittest

class TestRSelect(unittest.TestCase):
    def gen_data(self, n):
        """Return list of n-lists of 1 through n -1 random integers."""
        data = []
        for x in range(2, n):
            d = []
            for _ in range(x):
                d.append(randrange(-100, 1000))
            indice = randrange(1, len(d))
            data.append((d, indice))
        return data

    """ def test_bad_values(self):
        bad_data = (
            (None, None),
            ((1, 1), None),
            (('abc', 1), None)
        )
        for *args, expected in bad_data:
            self.assertEqual(rs(*args), expected) """

    def test_valid_values(self):
        data = self.gen_data(8)
        for args in data:
            array, i = args
            self.assertEqual(rs(array, i), sorted(array)[i - 1])


if __name__ == '__main__':
    unittest.main()