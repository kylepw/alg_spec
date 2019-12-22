"""Topological sort for Kosaraju algorithm"""

# Track of current topological value
curr_tval = None


def _dfs_topo(graph: list, start, visited: list, f: list):
    """DFS for finding strongly connected components.

        Args:
            graph: indices are vertices, values are lists of adjacent vertices
            start: vertex to start search from
            visited: list of visited vertices
            f: vertices (indices) and their topological order (value)
    """
    if not graph:
        return
    global curr_tval
    visited.append(start)
    print(graph, start)
    for adj in graph[start]:
        if adj not in visited:
            _dfs_topo(graph, adj, visited, f)
    curr_tval -= 1
    f[curr_tval] = start


def ts(graph: list) -> list:
    """Sort topical ordering of a DAG (directed acyclic graph).

        Args:
            graph: a DAG with a vertex (index) and list of outgoing edges (value).

        Returns:
            list of visited vertices in topological order (indices). If error, None.

        Examples:
            >>> ts([ 0, [2, 4], [3], [6], [5], [6], [] ])
            [1, 4, 5, 2, 3, 6]
    """
    if not graph:
        return

    global curr_tval
    # `graph` has nothing (0) in zero index
    curr_tval = len(graph) - 1
    f = [0] * (len(graph) - 1)
    visited = []
    for v in range(1, len(graph)):
        if v not in visited:
            _dfs_topo(graph, v, visited, f)
    # Reset
    curr_tval = None
    return f
