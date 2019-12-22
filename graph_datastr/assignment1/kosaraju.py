"""Kosaraju implementation."""
from ktopo import ts
import argparse
import os

# SCC label
num_scc = None

def dfs_scc(graph: dict, start, visited: list, scc: list):
    """Iterative DFS for finding strongly connected components.

        Args:
            graph: keys are vertices, values are lists of adjacent vertices
            target: node value to search for
            start: node to start search from
            visited: list of visited vertices
            scc: vertices (indices) and their component label (value)
    """
    if not graph:
        return
    global num_scc
    stack = [start]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            scc[v] = num_scc
            for adj in graph[v]:
                stack.append(adj)


def load_edges(path: str) -> dict:
    """Convert text file with two integers per line to list of edges.

        Args:
            path: file path

        Returns:
            List of directed edges (tuples)

        Raises:
            IOError if file not found or invalid data.
    """
    try:
        with open(path) as f:
            edges = [tuple(v.strip().split()[:2]) for v in f.readlines() if len(v) > 1]
            edges = [(int(x), int(y)) for x, y in edges]
    except IOError:
        raise IOError(f'{path} does not exist.')
    except ValueError:
        raise ValueError('Invalid file. Must contain two vertices per line.')

    return edges


def reverse_edges(edges: list) -> list:
    """Reverse list of edges (x, y) to (y, x).

        Args:
            List of directed edges (x, y)

        Returns:
            List of reversed directed edges (y, x)
    """
    return [(y, x) for x, y in edges]


def edges_to_list(edges: list) -> list:
    """Convert list of edges to list of vertices/outgoing adjacent vertices.

        Args:
            edges: list of directed edges (tuples)

        Returns:
            vertices/list of outgoing adjacent vertices (index/value)
    """
    # graph will have blank  in index 0 (vertices numbered from 1)
    count = []
    for x, y in edges:
        if x not in count:
            count.append(x)
        if y not in count:
            count.append(y)
    graph = [0] * (len(count) + 1)
    for tail, head in edges:
        if graph[tail] == 0:
            graph[tail] = []
        if graph[head] == 0:
            graph[head] = []
        if head not in graph[tail]:
            graph[tail].append(head)
    return graph


def top_scc(scc: list, n) -> list:
    """Return sizes of n largest SCCs.

        Args:
            scc: vertices (indices) and component labels (values)
            n: number of SCC sizes to return

        Returns:
            sizes of n largest SCCs
    """
    result = {}
    for c in scc:
        if c != 0:
            result[c] = result[c] + 1 if c in result else 1
    result = list(result.values())
    result.sort(reverse=True)
    result = result[:5]
    while len(result) < 5:
        result.append(0)
    return result[:5]


def get_parser():
    parser = argparse.ArgumentParser(
        description='Count SSC (strongly connected components) of graph from file'
    )
    parser.add_argument(
        'filename', metavar='file', help='file with two vertices per line'
    )
    return parser


def main():
    global num_scc

    parser = get_parser()
    args = vars(parser.parse_args())

    edges = load_edges(args['filename'])
    re_edges = reverse_edges(edges)

    # Original and reversed graphs
    graph = edges_to_list(edges)
    re_graph = edges_to_list(re_edges)

    # Compute topological ordering
    t_vals = ts(re_graph)

    # Find SCCs in reverse topological order
    if num_scc is None:
        num_scc = 0
    scc = [0] * (len(t_vals) + 1)
    visited = []
    for v in t_vals:
        if v not in visited:
            num_scc += 1
            dfs_scc(graph, v, visited, scc)
    # Reset
    num_scc = None


    print(top_scc(scc, 5))


if __name__ == '__main__':
    main()
