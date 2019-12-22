from ktopo import ts
import unittest


class TestTs(unittest.TestCase):
    def test_ts(self):
        data = (
            (
                [ 0, [2, 4], [3], [6], [5], [6], [] ],
                [1, 4, 5, 2, 3, 6]
            ),
        )
        for graph, expected in data:
            self.assertEqual(ts(graph), expected)


if __name__ == '__main__':
    unittest.main()
