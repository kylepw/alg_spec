"""Kosaraju implementation."""
import argparse
import os


# vertex labels range
NUM_VERT = 875715
#NUM_VERT = 6

# Track of current topological value
curr_tval = None


def load_edges(path: str):
    """Convert text file with two integers per line to list of edges.

        Args:
            path: file path

        Returns:
            List of directed edges (tuples)
    """
    global NUM_VERT
    graph = [[] for i in range(NUM_VERT)]
    re_graph = [[] for i in range(NUM_VERT)]
    with open(path) as f:
        for line in f:
            edges = line.split()
            graph[int(edges[0])].append(int(edges[1]))
            re_graph[int(edges[1])].append(int(edges[0]))

    return graph, re_graph


def ts(graph: list) -> list:
    """Sort topical ordering via DFS of a DAG (directed acyclic graph).

        Args:
            graph: a DAG with a vertex (index) and list of outgoing edges (value).
            stack: keep track of DFS stack

        Returns:
            list of visited vertices in topological order (indices). If error, None.
    """
    if not graph:
        return
    global NUM_VERT
    visited = [False for i in range(NUM_VERT)]
    order = []
    order_added = [False for i in range(NUM_VERT)]

    for start in range(1, NUM_VERT):
        if visited[start] is not True:
            stack = [start]
            tmp_stack = []
            while stack:
                s = stack.pop()
                if order_added[s] is not True:
                    tmp_stack.append(s)
                    order_added[s] = True
                if visited[s] is not True:
                    stack.extend(graph[s])
                    visited[s] = True
            while tmp_stack:
                order.append(tmp_stack.pop())
    return order


def dfs_scc(graph: dict, order: list):
    """Iterative DFS for finding strongly connected components.

        Args:
            graph: keys are vertices, values are lists of adjacent vertices
            target: node value to search for
            order: vertices in topological order
    """
    if not graph:
        return
    global NUM_VERT
    # Index is the scc leader and the value is the size of the scc.
    scc = [0 for i in range(NUM_VERT)]
    visited = [False for i in range(NUM_VERT)]

    order.reverse()
    # Component label
    for start in order:
        if visited[start] is not True:
            stack = [start]
            while stack:
                s = stack.pop()
                if visited[s] is not True:
                    scc[start] += 1
                    for v in graph[s]:
                        stack.append(v)
                    visited[s] = True

    return scc


def get_parser():
    parser = argparse.ArgumentParser(
        description='Count SSC (strongly connected components) of graph from file'
    )
    parser.add_argument(
        'filename', metavar='file', help='file with two vertices per line'
    )
    return parser


def main():
    global NUM_VERT

    parser = get_parser()
    args = vars(parser.parse_args())

    graph, re_graph = load_edges(args['filename'])

    # Compute topological ordering
    order = ts(re_graph)

    # Label SCCs in reverse topological order
    scc = dfs_scc(graph, order)

    # Top 5 largest SCCS
    scc.sort(reverse=True)
    print(scc[:5])


if __name__ == '__main__':
    main()
