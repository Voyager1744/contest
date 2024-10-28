def count_valid_sequences(N, s):
    MOD = 10 ** 9 + 7

    # Динамическое программирование: dp[i][j] - количество способов
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # Пустая последовательность

    for i in range(N):
        for j in range(N + 1):
            if dp[i][j] == 0:
                continue

            if s[i] == '?':
                # Можно заменить на '(', '[', '{'
                dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j] * 3) % MOD

                # Можно заменить на ')', ']', '}'
                if j > 0:
                    dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j] * 3) % MOD
            else:
                if s[i] in '([{':
                    dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % MOD
                elif s[i] in ')]}':
                    if j > 0:
                        dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j]) % MOD

    return dp[N][0]


# Чтение ввода
N = int(input().strip())
s = input().strip()

# Вывод результата
print(count_valid_sequences(N, s))
