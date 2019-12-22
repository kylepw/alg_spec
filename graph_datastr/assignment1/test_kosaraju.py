import kosaraju
import unittest
from unittest.mock import mock_open, patch


class TestLoadEdges(unittest.TestCase):
    def test_33110_data(self):
        data = '''
            1 2
            2 3
            3 1
            3 4
            5 4
            6 4
            8 6
            6 7
            7 8'''
        expected = [
            ('1', '2'),
            ('2', '3'),
            ('3', '1'),
            ('3', '4'),
            ('5', '4'),
            ('6', '4'),
            ('8', '6'),
            ('6', '7'),
            ('7', '8'),
        ]
        with patch('kosaraju.open', mock_open(read_data=data)):
            self.assertEqual(kosaraju.load_edges(data), expected)

    def test_alpha_data(self):
        data = '''
            A D
            B H
            C F
            D G
            E B
            F I
            G A
            H E
            H F
            I G
            I C'''
        expected = [
            ('A', 'D'),
            ('B', 'H'),
            ('C', 'F'),
            ('D', 'G'),
            ('E', 'B'),
            ('F', 'I'),
            ('G', 'A'),
            ('H', 'E'),
            ('H', 'F'),
            ('I', 'G'),
            ('I', 'C'),
        ]
        with patch('kosaraju.open', mock_open(read_data=data)):
            self.assertEqual(kosaraju.load_edges(data), expected)


class TestEdgesToList(unittest.TestCase):
    def test_33110_data(self):
        edges = [(1, 2), (2, 3), (3, 1), (3, 4), (5, 4), (6, 4), (8, 6), (6, 7), (7, 8)]
        expected = [0, [2], [3], [1, 4], [], [4], [4, 7], [8], [6]]

        self.assertEqual(kosaraju.edges_to_list(edges), expected)


class TestReverseEdges(unittest.TestCase):
    def test_33110_data(self):
        edges = [(1, 2), (2, 3), (3, 1), (3, 4), (5, 4), (6, 4), (8, 6), (6, 7), (7, 8)]
        expected = [
            (2, 1),
            (3, 2),
            (1, 3),
            (4, 3),
            (4, 5),
            (4, 6),
            (6, 8),
            (7, 6),
            (8, 7),
        ]

        self.assertEqual(kosaraju.reverse_edges(edges), expected)

    def test_alpha_data(self):
        edges = [
            ('A', 'D'),
            ('B', 'H'),
            ('C', 'F'),
            ('D', 'G'),
            ('E', 'B'),
            ('F', 'I'),
            ('G', 'A'),
            ('H', 'E'),
            ('H', 'F'),
            ('I', 'G'),
            ('I', 'C'),
        ]
        expected = [
            ('D', 'A'),
            ('H', 'B'),
            ('F', 'C'),
            ('G', 'D'),
            ('B', 'E'),
            ('I', 'F'),
            ('A', 'G'),
            ('E', 'H'),
            ('F', 'H'),
            ('G', 'I'),
            ('C', 'I'),
        ]

        self.assertEqual(kosaraju.reverse_edges(edges), expected)


if __name__ == '__main__':
    unittest.main()
