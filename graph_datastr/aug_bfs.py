"""Breadth-first search shortest path implementations."""

def bfs_shortest_path(graph, x, y):
    """Find shortest number of edges between nodes x and y.
        :x: a node
        :y: a node

        :Returns: shortest number of edges from node x to y or -1 if none exists
    """
    if x == y:
        return 0
    visited = [x]
    q = [x]
    # keep tab on distances from `x`
    dist = {x: 0, y: -1}
    while q:
        v = q.pop(0)
        if v == y:
            dist[y] = dist[v] if dist[y] == -1 else min(dist[y], dist[v])
        for a in graph[v]:
            if a not in visited:
                visited.append(a)
                dist[a] = dist[v] + 1
                q.append(a)
    return dist[y]

def bfs_shortest_path_print(graph, x, y):
    """Return shortest path between nodes x and y."""
    visited = []
    q = [[x]]

    while q:
        path = q.pop(0)
        node = path[-1]
        if node not in visited:
            for adjacent in graph[node]:
                new_path = list(path)
                new_path.append(adjacent)
                if adjacent == y:
                    return new_path
                q.append(new_path)
            visited.append(node)
    return f'No path from {x} to {y}.'


if __name__ == '__main__':
    graph = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['A', 'B', 'D'],
    'F': ['C'],
    'G': ['C'],
}
print(bfs_shortest_path(graph, 'G', 'D'))
print(bfs_shortest_path_print(graph, 'G', 'D'))