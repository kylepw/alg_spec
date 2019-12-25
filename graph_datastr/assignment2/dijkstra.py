"""
    dijkstra.py
    ~~~~~~~~~~~

    Dijkstra's shortest-path algorithm implementation.

    Usage:
    python dijkstra.py [data.txt]

    The file data.txt contains an adjacency list representation of an
    undirected weighted graph with 200 vertices labeled 1 to 200. Each row
    consists of the node tuples that are adjacent to that particular vertex
    along with the length of that edge. For example, the 6th row has 6 as the
    first entry indicating that this row corresponds to the vertex labeled 6.
    The next entry of this row "141,8200" indicates that there is an edge
    between vertex 6 and vertex 141 that has length 8200. The rest of the pairs
    of this row indicate the other vertices adjacent to vertex 6 and the
    lengths of the corresponding edges.

    Dijkstra's shortest-path algorithm is on this graph, using 1 (the first
    vertex) as the source vertex, and to compute the shortest-path distances
    between 1 and every other vertex of the graph. If there is no path between a
    vertex v and vertex 1, we'll define the shortest-path distance between 1 and
    v to be 1000000.

    Returns:
        Shortest-path distances to the following ten vertices, in order:
        7,37,59,82,99,115,133,165,188,197

"""
import argparse


def load_data(filename: str) -> list:
    """Load adjacency list of vertices from file."""
    graph = []

    return graph


def get_parser():
    parser = argparse.ArgumentParser(
        description='Return shortest-distances from vertex 1 to shortest-path distances to vertices, in order: 7,37,59,82,99,115,133,165,188,197'
    )
    parser.add_argument(
        'filename',
        metavar='file',
        help='file with vertices/adjacent vertices and distances',
    )
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    graph = load_data(args['filename'])

    print('Goodbye!')


if __name__ == '__main__':
    main()
