from bisect import bisect_left, bisect_right


def min_energy_cost(n, k, a):
    # Создаем список кортежей (значение, индекс)
    indexed_a = sorted((val, idx) for idx, val in enumerate(a))

    # Инициализируем массив результатов
    result = [0] * n

    # Префиксные суммы для значений в отсортированном массиве
    prefix_sums = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sums[i] = prefix_sums[i - 1] + indexed_a[i - 1][0]

    # Функция для нахождения минимальных энергозатрат
    def find_min_cost_for_index(i):
        original_value = a[i]
        pos = next(idx for idx, val in enumerate(indexed_a) if val[1] == i)

        # Определение k ближайших соседей
        left = pos - 1
        right = pos + 1
        selected = []

        while len(selected) < k:
            if left >= 0 and (right >= n or abs(indexed_a[left][0] - original_value) <= abs(
                    indexed_a[right][0] - original_value)):
                if indexed_a[left][1] != i:
                    selected.append(indexed_a[left][0])
                left -= 1
            else:
                if right < n and indexed_a[right][1] != i:
                    selected.append(indexed_a[right][0])
                right += 1

        # Вычисление энергозатрат
        min_cost = sum(abs(original_value - val) for val in selected)
        return min_cost

    # Вычисление результата для каждого индекса
    for i in range(n):
        result[i] = find_min_cost_for_index(i)

    return result


n, k = map(int, input().split())
a = list(map(int, input().split()))

result = min_energy_cost(n, k, a)

print(*result)
