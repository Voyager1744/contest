def find_min_lex_word(grid, R, C):
    words = []

    for row in grid:
        row_words = row.split('#')
        for word in row_words:
            if len(word) >= 2:
                words.append(word)

    for col in range(C):
        col_word = []
        for row in range(R):
            if grid[row][col] != '#':
                col_word.append(grid[row][col])
            else:
                if len(col_word) >= 2:
                    words.append("".join(col_word))
                col_word = []
        if len(col_word) >= 2:
            words.append("".join(col_word))

    return min(words)


R, C = map(int, input().split())
grid = [input().strip() for _ in range(R)]

print(find_min_lex_word(grid, R, C))
