"""Breadth-first search implementation."""
from queue import Queue
import unittest


def bfs(graph, value, start=None):
    """Breadth-first search

        graph (dic): keys are vertices, values are lists of adjacent vertices
        value: node value to search for
        start: node to start search from

        Return (bool): whether `value` is found or not.
    """
    if start is None:
        start = list(graph.keys())[0]
    visited = [start]
    q = Queue()
    q.put(start)
    while not q.empty():
        v = q.get()
        if v == value:
            return True
        for a in graph[v]:
            if a not in visited:
                visited.append(a)
                q.put(a)
    return False


class TestBfs(unittest.TestCase):
    def test_undirected_graph(self):
        graph = {
            1: [2, 4],
            2: [1, 6],
            3: [4],
            4: [1, 5, 6],
            5: [4],
            6: [2, 4, 7],
            7: [6],
        }

        self.assertTrue(bfs(graph, 7))
        self.assertFalse(bfs(graph, 8))

    @unittest.SkipTest
    def test_directed_graph(self):
        graph = {1: [2, 3], 2: [5], 3: [], 4: [2, 3], 5: [4]}

        self.assertTrue(bfs(graph, 4))
        self.assertFalse(bfs(graph, 0))


if __name__ == '__main__':
    unittest.main()
