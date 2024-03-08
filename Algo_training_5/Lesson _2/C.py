"""Петя, Маша и верёвочки"""
N = int(input())
lengths = list(map(int, input().split()))

max_length = max(lengths)

other = sum(lengths) - max_length
if other >= max_length:
    taken = sum(lengths)
else:
    taken = max_length - other

print(taken)

"""
4
1 5 2 1

1


4
5 12 4 3

24
"""