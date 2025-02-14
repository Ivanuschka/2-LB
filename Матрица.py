import random
import numpy as np
import matplotlib.pyplot as plt

def generate_random_matrix(rows, cols):
    """Генерация случайной бинарной матрицы"""
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

def count_islands(matrix):
    """Подсчёт количества островов в матрице"""
    if not matrix:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    
    def dfs(r, c):
        """Обход острова в глубину (DFS)"""
        if r < 0 or c < 0 or r >= rows or c >= cols or matrix[r][c] == 0 or visited[r][c]:
            return
        visited[r][c] = True
        # Проверяем 8 направлений (по горизонтали, вертикали и диагоналям)
        directions = [(-1, -1), (-1, 0), (-1, 1), 
                      (0, -1),        (0, 1), 
                      (1, -1), (1, 0), (1, 1)]
        for dr, dc in directions:
            dfs(r + dr, c + dc)

    island_count = 0
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1 and not visited[r][c]:
                dfs(r, c)
                island_count += 1  # Нашли новый остров
                
    return island_count

def plot_matrix(matrix):
    """Отображение матрицы с цветами (вода = синий, земля = коричневый)"""
    plt.figure(figsize=(5, 5))
    plt.imshow(matrix, cmap='copper', interpolation='nearest')
    plt.colorbar(label="0 - Вода | 1 - Земля")
    
    # Добавляем текстовые значения внутри клеток
    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            plt.text(j, i, str(matrix[i][j]), ha='center', va='center', color='white', fontsize=14)
    
    plt.xticks(range(cols))
    plt.yticks(range(rows))
    plt.title("Визуализация островов")
    plt.show()

# Генерируем случайную матрицу 5x5
rows, cols = 5, 5
random_matrix = generate_random_matrix(rows, cols)

# Подсчёт количества островов
islands = count_islands(random_matrix)

# Выводим матрицу в консоли
print("Случайная бинарная матрица:")
for row in random_matrix:
    print(" ".join(map(str, row)))
print(f"\nКоличество островов: {islands}")

# Визуализация
plot_matrix(random_matrix)
