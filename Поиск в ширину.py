from collections import deque

def bfs_shortest_path(graph, start, end):
    queue = deque([(start, 0)])  # (город, расстояние)
    visited = set()
    visited.add(start)
    
    while queue:
        node, distance = queue.popleft()
        if node == end:
            return distance
        
        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                queue.append((neighbor, distance + weight))
                visited.add(neighbor)
    
    return float('inf')  # Если путь не найден

graph = {
    'A': [('C', 10), ('J', 14), ('B', 15)],
    'B': [('A', 15), ('D', 12), ('H', 25)],
    'C': [('A', 10), ('D', 8), ('E', 20)],
    'D': [('C', 8), ('B', 12), ('E', 5), ('F', 18), ('G', 22)],
    'E': [('C', 20), ('D', 5), ('F', 18)],
    'F': [('D', 18), ('E', 18), ('G', 7)],
    'G': [('D', 22), ('F', 7), ('H', 10)],
    'H': [('G', 10), ('B', 25), ('I', 6)],
    'I': [('H', 6), ('J', 8)],
    'J': [('I', 8), ('A', 14)]
}

start = 'E'
end = 'I'
result = bfs_shortest_path(graph, start, end)
print(f"Кратчайший путь от {start} до {end}: {result} км")
