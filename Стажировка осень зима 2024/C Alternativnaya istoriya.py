def min_years_to_remove(n, events_A, events_B, events_C):
    # Уникальные события для каждой цивилизации
    unique_events_A = set(events_A)
    unique_events_B = set(events_B)
    unique_events_C = set(events_C)

    # Объединяем все события в одно множество
    all_events = unique_events_A | unique_events_B | unique_events_C

    # Переменная для минимального количества удалений
    min_removals = float('inf')
    best_years_to_remove = []

    # Перебираем все подмножества событий
    for event in all_events:
        # Проверяем, сколько нужно удалить для достижения целевого множества
        target_events = {event}  # текущее подмножество
        years_to_remove = []

        # Проходим по годам и определяем, что удалять
        for i in range(n):
            if (events_A[i] not in target_events and
                    events_B[i] not in target_events and
                    events_C[i] not in target_events):
                years_to_remove.append(i + 1)  # индексы с 1

        # Обновляем минимальное количество удалений
        if len(years_to_remove) < min_removals:
            min_removals = len(years_to_remove)
            best_years_to_remove = years_to_remove

    return min_removals, best_years_to_remove


# Пример использования
# n = 7
# events_A = [7, 6, 1, 2, 3, 4, 5]
# events_B = [7, 4, 3, 1, 1, 5, 5]
# events_C = [2, 6, 5, 4, 1, 7, 3]

n = int(input())
events_A = list(map(int, input().split()))
events_B = list(map(int, input().split()))
events_C = list(map(int, input().split()))

min_years, years = min_years_to_remove(n, events_A, events_B, events_C)
print(f"Минимальное количество лет для удаления: {min_years}")
print(f"Годы, информацию о которых нужно удалить: {years}")
