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
        {1: ['A', 'B', 'C', 'E', 'D', 'F', 'G'], 2: ['H', 'I', 'J'], 3: ['K']}
    """
    visited = []
    # Group each vertex with a component.
    components = {}
    # Component marker
    num_cc = 0
    for v in graph:
        if v not in visited:
            num_cc += 1
            components[num_cc] = [v]
            # BFS
            q = [v]
            visited.append(v)
            while q:
                current = q.pop(0)
                for a in graph[current]:
                    if a not in visited:
                        visited.append(a)
                        q.append(a)
                        components[num_cc].append(a)
    return components


if __name__ == '__main__':
    print(ucc(graph))