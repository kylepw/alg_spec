from ktopo import rts
import unittest

class TestRts(unittest.TestCase):
    def test_rts(self):
        data = (
            (
                {1: [5], 2: [9], 3: [1], 4: [2, 9], 5: [3], 6: [8, 11], 7: [4, 5], 8: [9, 10, 11], 9: [5, 7], 10: [6], 11: [3]},
                {1: 9, 2: 5, 3: 11, 4: 8, 5: 10, 6: 1, 7: 7, 8: 2, 9: 6, 10: 4, 11: 3}
            ),
        )
        for graph, expected in data:
            self.assertDictEqual(rts(graph, 6), expected)

if __name__ == '__main__':
    unittest.main()