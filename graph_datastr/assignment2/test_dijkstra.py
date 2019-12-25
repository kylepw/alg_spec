from dijkstra import get_parser
import unittest


class TestGetParser(unittest.TestCase):
    def setUp(self):
        self.parser = get_parser()
    def test_no_required_file_arg(self):
        with self.assertRaises(SystemExit):
            get_parser().parse_args([])

    def test_too_many_args(self):
        with self.assertRaises(SystemExit):
            get_parser().parse_args(['data.txt', 'data.txt'])


if __name__ == '__main__':
    unittest.main()
