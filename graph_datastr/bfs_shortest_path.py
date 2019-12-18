"""Breadth-first search shortest path implementation."""

def bfs_shortest_path(graph, x, y):
    """Find shortest path between nodes x and y.
        :x: a node
        :y: a node

        :Returns: None
    """
    visited = [x]
    q = [x]
    shortest = current = 0
    while q:
        v = q.pop(0)
        if v == y:
            shortest = min(shortest, current)
        for a in graph[v]:
            if a not in visited:
                visited.append(a)
                q.append(a)
        current += 1
    return shortest

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