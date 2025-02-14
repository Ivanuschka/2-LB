from collections import deque

def shortest_path(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Вверх, вниз, влево, вправо
    queue = deque([(start[0], start[1], 0)])  # (x, y, шаги)
    visited = set()
    visited.add(start)
    
    while queue:
        x, y, steps = queue.popleft()
        
        if (x, y) == end:
            return steps  # Возвращаем количество шагов до выхода
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1 and (nx, ny) not in visited:
                queue.append((nx, ny, steps + 1))
                visited.add((nx, ny))
    
    return -1  # Если путь не найден

maze = [
    [1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1]
]

start = (6, 0)
end = (4, 6)

result = shortest_path(maze, start, end)
print("Кратчайший путь от S к E:", result)
