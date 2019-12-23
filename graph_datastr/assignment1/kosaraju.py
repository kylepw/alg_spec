"""
    kosaraju.py
    ~~~~~~~~~~~

    Kosaraju implementation that reads a file of edges (two spaced integers
    per line).

    Usage:
        python kosaraju.py filename.txt

"""
import argparse


def load_edges(path: str) -> (list, int):
    """Convert text file with two integers per line to list of edges

        Args:
            path: file path

        Returns:
            List of edges (tuples), max vertex number plus one
    """
    edges = []
    MAX_VERT = -1

    with open(path) as f:
        for line in f:
            edge = line.split()
            if len(edge) == 2 and edge[0] != '#':
                x, y = int(edge[0]), int(edge[1])
                MAX_VERT = max(MAX_VERT, x, y)
                edges.append((x, y))

    return edges, MAX_VERT + 1


def create_graphs(edges: list, MAX_VERT: int):
    """Convert text file with two integers per line to list of edges.

        Args:
            edges: list of edges (tuples)
            MAX_VERT: max vertex number in graph plus one

        Returns:
            Graph and reversed version
    """
    graph = [[] for i in range(MAX_VERT)]
    re_graph = [[] for i in range(MAX_VERT)]

    for x, y in edges:
        graph[x].append(y)
        re_graph[y].append(x)

    return graph, re_graph


def ts(graph: list, MAX_VERT: int) -> list:
    """Sort topical ordering via DFS of a DAG (directed acyclic graph).

        Args:
            graph: a DAG with a vertex (index) and list of outgoing edges (value).
            MAX_VERT: max vertex number in graph plus one

        Returns:
            list of visited vertices in topological order (indices). If error, None.
    """
    if not graph:
        return
    visited = [False for i in range(MAX_VERT)]
    order = []

    for start in range(1, MAX_VERT):
        if visited[start] is False:
            stack = [start]
            tmp_stack = []
            while stack:
                s = stack.pop()
                if visited[s] is False:
                    stack.extend(graph[s])
                    tmp_stack.append(s)
                    visited[s] = True
            while tmp_stack:
                order.append(tmp_stack.pop())

    return order


def dfs_scc(graph: dict, order: list, MAX_VERT: int) -> list:
    """Iterative DFS for finding strongly connected components.

        Args:
            graph: keys are vertices, values are lists of adjacent vertices
            order: vertices in topological order
            MAX_VERT: max vertex number in graph plus one

        Returns:
            List of SCCs (indices) and number of vertices (values)
    """
    if not graph:
        return
    # Index is SCC leader and value the number of vertices in SCC.
    scc = [0 for i in range(MAX_VERT)]
    visited = [False for i in range(MAX_VERT)]

    order.reverse()
    for start in order:
        if visited[start] is False:
            stack = [start]
            while stack:
                s = stack.pop()
                if visited[s] is False:
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
    parser = get_parser()
    args = vars(parser.parse_args())

    edges, MAX_VERT = load_edges(args['filename'])
    graph, re_graph = create_graphs(edges, MAX_VERT)

    # Topological order
    order = ts(re_graph, MAX_VERT)

    # Label SCCs in reverse topological order
    scc = dfs_scc(graph, order, MAX_VERT)

    # Top 5 largest SCCs
    scc.sort(reverse=True)
    print(scc[:5])


if __name__ == '__main__':
    main()
