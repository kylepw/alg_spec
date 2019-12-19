"""Undirected connected component search implementation."""
graph = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['A', 'B', 'D'],
    'F': ['C'],
    'G': ['C'],
    'H': ['I'],
    'I': ['H', 'J'],
    'J': ['I'],
    'K': ['K']
}

def ucc(graph):
    """Identify connected components in undirected graph.

        Examples:
        >>> ucc(graph)
    """
    q = []
    visited = []
    # Mark each vertex in a component.
    components = {}
    for v in graph:
        if v not in visited:
            s = v
            components[s] = []
            q.append(v)
        while q:
            current = q.pop(0)
            for a in graph[current]:
                if a not in visited:
                    visited.append(a)
                    q.append(a)
                    components[s].append(current)
    return components


if __name__ == '__main__':
    print(ucc(graph))