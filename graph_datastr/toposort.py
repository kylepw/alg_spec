"""Topical sort implementation."""

graph = {
    'A': ['B', 'D'],
    'B': ['C'],
    'C': ['F'],
    'D': ['E'],
    'E': ['F'],
    'F': [],
}

curr_tval = None

def dfs_topo(graph: dict, start, visited: dict):
    """Labels graph vertices with topological values.

        Args:
            graph: keys are vertices, values are lists of adjacent vertices
            start: node to start search from
            visited: visited nodes (keys) and topological values (values)
    """
    global curr_tval
    if not graph or not start or start not in graph:
        return
    if curr_tval is None:
        curr_tval = len(graph)
    visited[start] = None
    for adj in graph[start]:
        if adj not in visited:
            dfs_topo(graph, adj, visited)
    visited[start] = curr_tval
    curr_tval -= 1


def ts(graph: dict, start):
    """Sort topical ordering of a DAG (directed acyclic graph).

        Args:
            graph: a DAG with a vertex (key) and list of outgoing edges (value).

        Returns:
            dict of visited vertices and assigned topological values. If error, None.

        Examples:
            >>> ts(graph)
            {'A': 1, 'B': 4, 'C': 5, 'F': 6, 'D': 2, 'E': 3}
    """
    if not graph or not start or start not in graph:
        return
    visited = {}
    for v in graph:
        if v not in visited:
            dfs_topo(graph, v, visited)
    return visited


if __name__ == '__main__':
    print(ts(graph, 'A'))