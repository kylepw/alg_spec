from dijkstra import dsp, get_parser, load_data
import unittest
from unittest.mock import mock_open, patch


class TestLoadData(unittest.TestCase):
    def test_data(self):
        data = '''
            1   80,982	163,8164	170,2620	145,648
            2   42,1689	127,9365	5,8026	170,9342
        '''
        expected = [
            [],
            [(80, 982), (163, 8164), (170, 2620), (145, 648)],
            [(42, 1689), (127, 9365), (5, 8026), (170, 9342)],
        ]
        with patch('dijkstra.open', mock_open(read_data=data)):
            graph = load_data(data)
            self.assertEqual(graph, (expected))
            self.assertEqual(len(graph), 3)


class TestGetParser(unittest.TestCase):
    def setUp(self):
        self.parser = get_parser()

    def test_no_required_file_arg(self):
        with self.assertRaises(SystemExit):
            get_parser().parse_args([])

    def test_too_many_args(self):
        with self.assertRaises(SystemExit):
            get_parser().parse_args(['data.txt', 'data.txt'])


class TestDsp(unittest.TestCase):
    def setUp(self):
        self.graph = [[], [(2, 1)], [(3, 1)], [(4, 1)], [(5, 3)], []]

    def test_same_start_and_target(self):
        self.assertEqual(dsp(self.graph, 1, 1), 0)

    def test_distance_1_to_4(self):
        self.assertEqual(dsp(self.graph, 1, 4), 3)

    def test_distance_3_to_5(self):
        self.assertEqual(dsp(self.graph, 3, 5), 4)


if __name__ == '__main__':
    unittest.main()
