import kosaraju
import unittest
from unittest.mock import mock_open, patch

class TestFileToGraph(unittest.TestCase):
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
        expected = {1: [2], 2: [3], 3: [1, 4], 5: [4], 6: [4, 7], 8: [6], 7: [8]}
        with patch('kosaraju.open', mock_open(read_data=data)):
            self.assertEqual(kosaraju.file_to_graph(data), expected)

    def test_33200_data(self):
        data = '''
            1 2
            2 6
            2 3
            2 4
            3 1
            3 4
            4 5
            5 4
            6 5
            6 7
            7 6
            7 8
            8 5
            8 7'''
        expected = {1: [2], 2: [6, 3, 4], 3: [1, 4], 4: [5], 5: [4], 6: [5, 7], 7: [6, 8], 8: [5, 7]}
        with patch('kosaraju.open', mock_open(read_data=data)):
            self.assertEqual(kosaraju.file_to_graph(data), expected)

    def test_33300_data(self):
        data = '''
            1 4
            2 8
            3 6
            4 7
            5 2
            6 9
            7 1
            8 5
            8 6
            9 7
            9 3'''
        expected = {1: [4], 2: [8], 3: [6], 4: [7], 5: [2], 6: [9], 7: [1], 8: [5, 6], 9: [7, 3]}
        with patch('kosaraju.open', mock_open(read_data=data)):
            self.assertEqual(kosaraju.file_to_graph(data), expected)

if __name__ == '__main__':
    unittest.main()