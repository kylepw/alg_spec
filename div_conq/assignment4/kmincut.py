"""
    kmincut.py
    ~~~~~~~~~~

    Karser contraction algorithm min cutimplementation.

    Note: Graph data is represented by rows of numbers. First column
    is a vertex. Subsequent columns represent its adjacent vertices.
    1 45 3 2
    2 1 5 66
    3 ...
"""
import argparse
import random
import time


def get_parser():
    parser = argparse.ArgumentParser(
        description="Find minimum cut of graph with Karger's algorithm."
    )
    parser.add_argument('filename', metavar='file', help='file with graph data')
    return parser


def load_vdata(filename):
    """Load vertice data into dict."""
    vertices = {}
    with open(filename) as f:
        for line in f:
            l = [int(n) for n in line.split()]
            vertices[l[0]] = l[1:]
    return vertices


def kmc(graph):
    """
        Return graph's min cut with Karger's random contraction algorithm.

        graph (dict): key/value pairs of vertices/set of adjacent vertices

        Return (int): min cut
    """
    while len(graph) > 2:
        # Choose random edge
        v1 = random.choice(list(graph.keys()))
        v2 = random.choice(graph[v1])
        while v2 not in graph:
            v2 = random.choice(graph[v1])
        # Collapse v2 vertex into v1 vertex in graph.
        graph[v1].extend([v for v in graph[v2] if v != v1])
        graph[v1].remove(v2)
        for v in graph[v2]:
            if v in graph and v != v1:
                for i, a in enumerate(graph[v]):
                    if a == v2:
                        graph[v][i] = v1
        del graph[v2]
    result = []
    last1 = list(graph.keys())[0]
    last2 = list(graph.keys())[1]
    # Find connections
    result = [v for v in graph[last1] if v == last2]
    return len(result)


if __name__ == '__main__':
    parser = get_parser()
    args = vars(parser.parse_args())
    try:
        graph = load_vdata(args['filename'])
        print(kmc(graph))
    except IOError:
        print(f"Failed to open {args['file']}")
        exit(1)
