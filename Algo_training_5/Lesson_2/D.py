"""Шахматная доска"""
"""Из шахматной доски по границам клеток выпилили связную (не распадающуюся на части)
 фигуру без дыр. Требуется определить ее периметр."""


def calculate_perimeter(cells):
    perimeter = 0
    for cell in cells:
        row, col = cell
        perimeter += 4

        if (row - 1, col) in cells:
            perimeter -= 1
        if (row + 1, col) in cells:
            perimeter -= 1
        if (row, col - 1) in cells:
            perimeter -= 1
        if (row, col + 1) in cells:
            perimeter -= 1

    return perimeter


n = int(input())
cells = []
for _ in range(n):
    row, col = map(int, input().split())
    cells.append((row, col))


perimeter = calculate_perimeter(cells)
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