#!/usr/bin/env python3
"""Prim's minimum spanning tree algorithm.

edges.txt file describes an undirected graph with integer edge costs. It has
the format:

[number_of_nodes] [number_of_edges]

[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]

[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]

...

For example, the third line of the file is "2 3 -8874", indicating that there
is an edge connecting vertex #2 and vertex #3 that has cost -8874.

You should NOT assume that edge costs are positive, nor should you assume that
they are distinct.

Your task is to run Prim's minimum spanning tree algorithm on this graph. You
should report the overall cost of a minimum spanning tree --- an integer,
which may or may not be negative --- in the box below.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn)
time implementation of Prim's algorithm should work fine. OPTIONAL: For those
of you seeking an additional challenge, try implementing a heap-based version.
The simpler approach, which should already give you a healthy speed-up, is to
maintain relevant edges in a heap (with keys = edge costs). The superior
approachstores the unprocessed vertices in the heap, as described in lecture.
Note this requires a heap that supports deletions, and you'll probably need to
maintain some kind of mapping between vertices and their positions in the heap.
"""
import argparse
from collections import defaultdict


def extract_graph(filename):
    """Extract graph data from file.

        Args:
            filename

        Returns:
            Tuple of:
            - dict of vertices with adjacency lists {'A': ['C', 'D'], ...}
            - dict of edges {(vertex1, vertex2): edge cost, ...}
    """
    with open(filename) as f:
        vert_count, edge_count = [int(c) for c in f.readline().split()]

        vertices = defaultdict(set)
        edges = {}
        for line in f:
            v1, v2, cost = [int(e) for e in line.split()]
            vertices[v1].add(v2)
            vertices[v2].add(v1)
            edges[(v1, v2)] = cost
            edges[(v2, v1)] = cost

    assert len(vertices) == vert_count
    # Includes (v1, v2) and (v2, v1) edges
    assert len(edges) == edge_count * 2

    return vertices, edges


def get_mst(vertices, edges):
    """Use Prim's minimum spanning tree algorithm to find MST of graph.

        Args:
            vertices (dict): adjacent list of vertices {v: [w, ...], ...}
            edges (dict): edges in form {(v1, v2): cost, ...}

        Returns:
            dict of minimum spanning tree edges and costs {(v1, v2): cost, ...}
    """
    unvisited = [v for v in vertices.keys()]
    visited = [unvisited.pop()]
    mst_edges = {}

    while unvisited:
        current_min = None
        min_vw = None
        for v in visited:
            for w in vertices[v]:
                if w in visited:
                    continue
                if current_min is None:
                    min_vw = (v, w)
                    current_min = edges[min_vw]
                else:
                    prev_min = current_min
                    current_min = min(current_min, edges[(v, w)])
                    if prev_min > current_min:
                        min_vw = (v, w)
        visited.append(unvisited.pop(unvisited.index(min_vw[1])))
        mst_edges[min_vw] = edges[min_vw]

    return mst_edges


def get_parser():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('filename', metavar='edges.txt', help='')
    return parser


def main():
    parser = get_parser()
    parsed = vars(parser.parse_args())

    vertices, edges = extract_graph(parsed['filename'])

    tree = get_mst(vertices, edges)

    # Overall cost of MST
    print(sum(tree.values()))


if __name__ == '__main__':
    main()
