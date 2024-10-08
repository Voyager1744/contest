"""
Создатели расширяют Вселенную Яндекса, сотворяя новые Миры. Для создания Миров нужно заполнить
 пространственные пустоты Энергией.

Создатели обнаружили
n бесконечно больших пространственных пустот, расположенных в один ряд. Пустоты по форме напоминают
 колбы. Изначально в каждой из пространственных пустот уже находится некоторое количество Энергии.
 Правила техники безопасности гласят, что для предотвращения коллапса объём Энергии во всех
 пространственных пустотах должен быть одинаковым. Также по правилам, нельзя извлекать уже залитую
 Энергию из пустот.

Заполнять пустоты вручную — долго и ненадёжно. Поэтому Создатели изобрели промышленный разливатель.
За одну операцию он способен разлить по одному грамму Энергии в каждую из первых
k (1≤k≤n) пустот. Для разных операций
k могут быть разными.
Создатели просят вашей помощи. Помогите узнать, можно ли налить одинаковый объём Энергии во все
пространственные пустоты. Если это возможно, посчитайте минимальное количество операций, которое
потребуется, чтобы этого достичь.
"""


def is_non_decreasing(arr):
    return all(arr[i] >= arr[i - 1] for i in range(1, len(arr)))


n = int(input())
a = list(map(int, input().split()))

if not is_non_decreasing(a):
    print(-1)
else:
    ans = a[-1] - a[0]
    print(ans)

"""
3
1 2 3

5
1 1 1 5 5
"""