"""Topological sort for Kosaraju algorithm"""

# Track of current topological value
curr_tval = None

def dfs_topo(graph: dict, start, visited: dict):
    """Labels graph vertices with topological values in REVERSE ORDER.

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
    # Reverse
    tails = graph[start]
    visited[start] = None
    for t in tails:
        if t not in visited:
            visited[t] = None
        for adj in graph[t]:
            if adj not in visited:
                dfs_topo(graph, adj, visited)
        visited[t] = curr_tval
        curr_tval -= 1
    visited[start] = curr_tval


def rts(graph: dict, start):
    """Reverse a DAG (directed acyclic graph) and sort topological ordering.

        Args:
            graph: a DAG with a vertex (key) and list of outgoing edges (value).

        Returns:
            dict of visited vertices and assigned topological values. If error, None.
    """
    if not graph or not start or start not in graph:
        return
    visited = {}
    for v in graph:
        if v not in visited:
            dfs_topo(graph, v, visited)
    return visited