# Generic graph search

if __name__ == '__main__':
    V = ['A', 'B', 'C', 'D', 'E']
    E = {'A': ['B', 'E'], 'B': ['D'], 'C': ['E'], 'D': [], 'E': ['C']}

    start = V[0] # 'A'
    queue = [start]
    connected = [start]

    while queue:
        current = queue.pop()
        for adjacent in E[current]:
            if adjacent not in connected:
                queue.append(adjacent)
        if current not in connected:
            connected.append(current)
    print(f'Connections to {start}: {connected}')


