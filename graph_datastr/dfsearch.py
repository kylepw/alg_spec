"""Depth-first search algorithm implementations."""
graph = {
    1: [2, 4],
    2: [1, 6],
    3: [4],
    4: [1, 5, 6],
    5: [4],
    6: [2, 4, 7],
    7: [6],
}

def dfs_iter(graph: dict, target, start=None) -> bool:
    """Iterative DFS.

        Args:
            graph: keys are vertices, values are lists of adjacent vertices
            target: node value to search for
            start: node to start search from

        Examples:
        >>> dfs_iter(graph, 7)
        True
        >>> dfs_iter(graph, 8)
        False

        Returns:
            True if `target` found. Otherwise, False.
    """
    if not graph or target not in graph or (start is not None and start not in graph):
        return False
    if start is None:
        start = list(graph.keys())[0]
    stack = [start]
    visited = []
    while stack:
        v = stack.pop()
        if v == target:
            return True
        if v not in visited:
            visited.append(v)
            for adj in graph[v]:
                stack.append(adj)
    return False

def dfs_re(graph: dict, target, start=None, visited=None) -> bool:
    """Recursive DFS.

        Args:
            graph: keys are vertices, values are lists of adjacent vertices
            target: node value to search for
            start: node to start search from

        Examples:
            >>> dfs_iter(graph, 7)
            True
            >>> dfs_iter(graph, 8)
            False


        Returns:
            True if `target` found. Otherwise, False.
    """
    if not graph or target not in graph or (start is not None and start not in graph):
        return False
    if start is None:
        start = list(graph.keys())[0]
    if visited is None:
        visited = []

    visited.append(start)
    for adj in graph[start]:
        if adj not in visited:
            dfs_re(graph, target, adj, visited)
    return target in visited


if __name__ == '__main__':
    v = 7
    print(f"{v} in graph?")
    print(dfs_iter(graph, v))
    print(dfs_re(graph, v))
