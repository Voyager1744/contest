"""Расписание"""

import calendar
from datetime import datetime, timedelta


# Функция для определения дня недели по дате
def day_of_week(year, month, day):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[datetime(year, month, day).weekday()]


# Функция для определения количества выходных дней в году
def count_weekends(year, holidays, chosen_weekday):
    total_days = 365 + len(holidays)
    weekends = 0

    # Подсчет выходных дней, включая государственные праздники и выбранный выходной день
    for day in range(1, 32):
        for month in range(1, 13):
            try:
                current_day = datetime(year, month, day)
                current_weekday = day_of_week(year, month, day)

                if current_weekday == chosen_weekday or current_day in holidays:
                    weekends += 1

            except ValueError:
                break

    return weekends


# Ввод данных
N = int(input())
year = int(input())
holidays = set()

for _ in range(N):
    day, month = input().split()
    holidays.add(datetime(year, list(calendar.month_name).index(month), int(day)))

first_day_of_year = input().strip()

# Расчет для каждого возможного выходного дня
possible_weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
max_weekends = 0
min_weekends = float('inf')

best_weekday = ""
worst_weekday = ""

for chosen_weekday in possible_weekdays:
    weekends = count_weekends(year, holidays, chosen_weekday)

    if weekends > max_weekends:
        max_weekends = weekends
        best_weekday = chosen_weekday

    if weekends < min_weekends:
        min_weekends = weekends
        worst_weekday = chosen_weekday

# Вывод результата
print(best_weekday, worst_weekday)

"""
2
2015
1 January
8 January
Thursday


3
2013
6 February
13 February
20 February
Tuesday


"""
