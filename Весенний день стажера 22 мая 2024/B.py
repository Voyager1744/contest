def max_friends_invited(n, t, friends):
    # Сортируем друзей по координатам
    friends.sort(key=lambda x: x[0])

    # Инициализируем массив для хранения максимального количества друзей
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        for j in range(i - 1, -1, -1):
            distance = abs(friends[i - 1][0] - friends[j][0])
            if t >= distance:
                dp[i] = max(dp[i], dp[j] + min(t - distance, friends[i - 1][1]))

    return dp[n]


# Чтение входных данных
n, T = map(int, input().split())
friends = []
for _ in range(n):
    x, t = map(int, input().split())
    friends.append((x, t))

# Вывод результата
print(max_friends_invited(n, T, friends))
