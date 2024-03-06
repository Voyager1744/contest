n, m = map(int, input().split())
c = int(input())
commands = input()

# Создаем граф
graph = {}

# Добавляем ребра между соседними точками
for i in range(n):
    for j in range(m):
        graph[(i, j)] = []
        if i > 0:
            graph[(i, j)].append((i - 1, j))  # Левая точка
        if i < n - 1:
            graph[(i, j)].append((i + 1, j))  # Правая точка
        if j > 0:
            graph[(i, j)].append((i, j - 1))  # Нижняя точка
        if j < m - 1:
            graph[(i, j)].append((i, j + 1))  # Верхняя точка

# Подсчитываем количество ребер, представляющих отрезки
segments_count = 0
current_vertex = (0, 0)
for command in commands:
    next_vertex = None
    if command == 'U' and current_vertex is not None:
        if current_vertex[1] < m - 1:
            next_vertex = (current_vertex[0], current_vertex[1] + 1)
    elif command == 'D' and current_vertex is not None:
        if current_vertex[1] > 0:
            next_vertex = (current_vertex[0], current_vertex[1] - 1)
    elif command == 'R' and current_vertex is not None:
        if current_vertex[0] < n - 1:
            next_vertex = (current_vertex[0] + 1, current_vertex[1])
    elif command == 'L' and current_vertex is not None:
        if current_vertex[0] > 0:
            next_vertex = (current_vertex[0] - 1, current_vertex[1])

    if next_vertex and next_vertex in graph.get(current_vertex, []):
        segments_count += 1
    current_vertex = next_vertex

print(segments_count)
