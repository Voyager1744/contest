def count_subarrays_with_median(n, b, a):
    # Найдем индекс числа B
    target_idx = a.index(b)

    # Преобразуем массив: считаем +1 для >= B и -1 для < B
    transformed = [1 if x >= b else -1 for x in a]

    # Словари для хранения префиксных балансов
    left_balance_counts = {0: 1}
    balance = 0
    count = 0

    # Префиксный проход влево от B (не включая его)
    for i in range(target_idx - 1, -1, -1):
        balance += transformed[i]
        if (target_idx - i) % 2 == 1:
            count += left_balance_counts.get(balance, 0)
        left_balance_counts[balance] = left_balance_counts.get(balance, 0) + 1

    # Обнуляем баланс и используем правый префиксный баланс
    balance = 0
    right_balance_counts = {0: 1}

    # Префиксный проход вправо от B (включительно)
    for i in range(target_idx, n):
        balance += transformed[i]
        if (i - target_idx + 1) % 2 == 1:
            count += right_balance_counts.get(balance, 0)
        right_balance_counts[balance] = right_balance_counts.get(balance, 0) + 1

    return count


# Примеры
print(count_subarrays_with_median(5, 2, [5, 4, 3, 2, 1]))  # Ожидаемый вывод: 2
print(count_subarrays_with_median(6, 3, [3, 6, 5, 4, 2, 1]))  # Ожидаемый вывод: 1
print(count_subarrays_with_median(7, 4, [5, 7, 2, 4, 3, 1, 6]))  # Ожидаемый вывод: 4
