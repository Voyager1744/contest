def get_card_count(n, k, cards) -> int:
    # Считаем сумму первых left карт слева
    left_sum = [0] * (k + 1)
    for i in range(1, k + 1):
        left_sum[i] = left_sum[i - 1] + cards[i - 1]

    # Считаем сумму right карт справа
    right_sum = [0] * (k + 1)
    for i in range(1, k + 1):
        right_sum[i] = right_sum[i - 1] + cards[-i]

    # Ищем максимальную сумму комбинаций карт слева и справа
    max_sum = 0
    for left in range(k + 1):
        right = k - left
        current_sum = left_sum[left] + right_sum[right]
        max_sum = max(max_sum, current_sum)

    return max_sum


# Пример использования:
n = int(input())  # количество карточек
k = int(input())  # количество ходов
cards = list(map(int, input().split()))  # список карточек

print(get_card_count(n, k, cards))
