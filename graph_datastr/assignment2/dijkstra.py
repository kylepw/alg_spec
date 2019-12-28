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
from minheap import MinHeap


def load_data(filename: str) -> list:
    """Load adjacency list of vertices from file.

        Args:
            filename: name of file with edge data in ascending order
        Returns:
            [(head, edge_val), ...] where each index represents a vertex tail
    """
    with open(filename) as f:
        data = []
        MAX_VERT = -1
        for line in f:
            v = line.split()
            if v and v[0].isdigit():
                v = [tuple(n.split(',')) if not n.isdigit() else int(n) for n in v]
                MAX_VERT = max(MAX_VERT, v[0])
                data.append(v)
        # Plus one so graph[MAX_VERT] works
        graph = [[] for i in range(MAX_VERT + 1)]
        for v in data:
            graph[v[0]] = [(int(head), int(weight)) for head, weight in v[1:]]

    return graph


def dsp_non_heap(graph: list, s, t) -> int:
    """
        Find shortest path from two vertices via Dijkstra's shortest-path algorithm
        without a min-heap.

        Args:
            s: source vertex
            t: the target vertex

        Returns:
            Shortest path from `s` to `t` vertices
    """
    if s == t:
        return 0

    VERT_NUM = len(graph) - 1

    # Vertices seen so far
    X = [s]
    # Shortest path values (i.e. shortest path to vertex 4 is a[4])
    A = [1000000 for i in range(len(graph))]
    A[s] = 0

    while len(X) < VERT_NUM:
        V, W, W_dist = -1, -1, -1
        for v in X:
            for w, dist in [(w, dist) for w, dist in graph[v] if w not in X]:
                if V == -1 or A[v] + dist < W_dist:
                    V, W, W_dist = v, w, (A[v] + dist)
        if V != -1:
            X.append(W)
            A[W] = W_dist
            if W == t:
                return A[W]
    return A[t]


def dsp(graph: list, s, t) -> int:
    """
        Find shortest path from two vertices via Dijkstra's shortest-path algorithm.

        Args:
            s: source vertex
            t: the target vertex

        Returns:
            Shortest path from `s` to `t` vertices
    """
    if s == t:
        return 0

    # Vertices seen so far
    visited = []
    A = [[] for i in range(len(graph))]
    heap = MinHeap([(0, s)])

    while not heap.is_empty():
        dist, u = heap.pop()
        if u in visited:
            continue
        visited.append(u)
        A[u] = dist
        if t == u:
            return A[u]
        for v, d in graph[u]:
            if v in visited:
                continue
            heap.insert((dist + d, v))
            A[v] = dist + d
    return A[t]


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

    # 2599,2610,2947,2052,2367,2399,2029,2442,2505,3068
    vertices = (7, 37, 59, 82, 99, 115, 133, 165, 188, 197)
    print(','.join([str(dsp(graph, 1, v)) for v in vertices]))
    #print(','.join([str(dsp_non_heap(graph, 1, v)) for v in vertices]))



if __name__ == '__main__':
    main()
