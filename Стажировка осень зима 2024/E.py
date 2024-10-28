def common_prefix_length(word1, word2):
    length = 0
    # Сравниваем два слова по символам до тех пор, пока они равны
    while length < len(word1) and length < len(word2) and word1[length] == word2[length]:
        length += 1
    return length


# Чтение входных данных
N = int(input())
words = [input().strip() for _ in range(N)]

Q = int(input())
results = []

# Обработка запросов
for _ in range(Q):
    query = input().strip()
    total_actions = 0
    found = False

    for word in words:
        total_actions += 1  # Сравнение с текущим словом
        prefix_length = common_prefix_length(word, query)
        total_actions += prefix_length  # Добавляем длину общего префикса

        if word == query:
            found = True
            break

    # Если слово не найдено, добавляем длину запроса
    if not found:
        total_actions += len(query)

    results.append(total_actions)

# Вывод результатов
for result in results:
    print(result)
