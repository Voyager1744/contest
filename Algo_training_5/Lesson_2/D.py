"""Шахматная доска"""
"""Из шахматной доски по границам клеток выпилили связную (не распадающуюся на части)
 фигуру без дыр. Требуется определить ее периметр."""


# def calculate_perimeter(cells):
#     perimeter = 0
#     for cell in cells:
#         row, col = cell
#         perimeter += 4
#
#         if (row - 1, col) in cells:
#             perimeter -= 1
#         if (row + 1, col) in cells:
#             perimeter -= 1
#         if (row, col - 1) in cells:
#             perimeter -= 1
#         if (row, col + 1) in cells:
#             perimeter -= 1
#
#     return perimeter
#
#
# n = int(input())
# cells = []
# for _ in range(n):
#     row, col = map(int, input().split())
#     cells.append((row, col))
#
#
# perimeter = calculate_perimeter(cells)
# print(perimeter)

n = int(input())
field = [[0] * 10 for _ in range(10)]

for _ in range(n):
    i, j = map(int, input().split())
    field[i][j] = 1

perimeter = 0

for i in range(1, 10):
    for j in range(1, 10):
        perimeter += field[i][j -1 ] != field[i][j]
        perimeter += field[i - 1][j] != field[i][j]

print(perimeter)


"""
3
1 1
1 2
2 1

8


1
8 8

4
"""