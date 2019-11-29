from karatsuba import kmult, kmult_pad
from random import randint, seed
import unittest

class TestKaratsubaMult(unittest.TestCase):
    def test_bad_values(self):
        pass
    def test_one_digit(self):
        seed(1)
        for _ in range(10):
            x = randint(1, 9)
            y = randint(1, 9)
            self.assertEqual(kmult(x, y), x * y)
    def test_two_digits(self):
        seed(1)
        for _ in range(100):
            x = randint(10, 99)
            y = randint(10, 99)
            self.assertEqual(kmult(x, y), x * y)
    def test_three_digits(self):
        seed(1)
        for _ in range(100):
            x = randint(100, 999)
            y = randint(100, 999)
            self.assertEqual(kmult(x, y), x * y)
    def test_six_digits(self):
        seed(1)
        for _ in range(100):
            x = randint(100000, 999999)
            y = randint(100000, 999999)
            print(x, y)
            self.assertEqual(kmult(x, y), x * y)

class TestKaratsubaMultPad(unittest.TestCase):
    def test_bad_values(self):
        pass
    def test_one_digit(self):
        seed(1)
        for _ in range(10):
            x = randint(1, 9)
            y = randint(1, 9)
            self.assertEqual(kmult_pad(x, y), x * y)
    def test_two_digits(self):
        seed(1)
        for _ in range(10):
            x = randint(10, 99)
            y = randint(10, 99)
            self.assertEqual(kmult_pad(x, y), x * y)
    def test_three_digits(self):
        seed(1)
        for _ in range(10):
            x = randint(100, 999)
            y = randint(100, 999)
            self.assertEqual(kmult_pad(x, y), x * y)
    def test_six_digits(self):
        seed(1)
        for _ in range(10):
            x = randint(100000, 999999)
            y = randint(100000, 999999)
            print(x, y)
            self.assertEqual(kmult_pad(x, y), x * y)

if __name__ == '__main__':
    unittest.main()