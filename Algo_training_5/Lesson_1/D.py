"""Слоны и ладьи"""

board = [list(input()[:8]) for _ in range(8)]

count = 0


def mark_bishop_attack(board, bishop_position):
    row, col = bishop_position
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    for direction in directions:
        r, c = row + direction[0], col + direction[1]

        while 0 <= r < len(board) and 0 <= c < len(board[0]):

            if board[r][c] in ["R", "B"]:
                break

            board[r][c] = "_"
            r += direction[0]
            c += direction[1]


def mark_rook_attack(board, rook_position):
    row, col = rook_position

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for direction in directions:
        r, c = row + direction[0], col + direction[1]

        while 0 <= r < len(board) and 0 <= c < len(board[0]):

            if board[r][c] in ["R", "B"]:
                break

            board[r][c] = "_"
            r += direction[0]
            c += direction[1]


for i in range(8):
    for j in range(8):
        if board[i][j] == 'B':
            mark_bishop_attack(board, (i, j))
        elif board[i][j] == 'R':
            mark_rook_attack(board, (i, j))

for i in range(8):
    for j in range(8):
        if board[i][j] == '*':
            count += 1

print(count)
