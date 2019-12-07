from random import randrange
from rselect import rs
import unittest

class TestRSelect(unittest.TestCase):
    def gen_data(self, n):
        """Return list of n-tuples (list of 1 through n -1 random integers, index)"""
        data = []
        for x in range(2, n):
            d = []
            for _ in range(x):
                d.append(randrange(-100, 1000))
            i = randrange(1, len(d))
            data.append((d, i))
        return data

    def test_valid_values(self):
        data = self.gen_data(8)
        for args in data:
            print(args)
            array, i = args
            expected = array[:]
            print(sorted(expected)[i - 1])
            self.assertEqual(rs(array, i), sorted(expected)[i - 1])


if __name__ == '__main__':
    unittest.main()