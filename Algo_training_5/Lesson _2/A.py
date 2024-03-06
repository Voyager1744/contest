"""Минимальный прямоугольник"""

k = int(input())
in_list = []
for _ in range(k):
    x, y = map(int, input().split())
    in_list.append((x, y))

x_min = min(in_list, key=lambda x: x[0])
y_min = min(in_list, key=lambda x: x[1])

x_max = max(in_list, key=lambda x: x[0])
y_max = max(in_list, key=lambda x: x[1])

print(x_min[0], y_min[1], x_max[0], y_max[1])

"""
4
1 3
3 1
3 5
6 3

1 1 6 5
"""