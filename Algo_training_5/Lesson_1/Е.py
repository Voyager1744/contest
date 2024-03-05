"""Прибыльный стартап"""

import sys

PYTHONINTMAXSTRDIGITS = 1000000
sys.set_int_max_str_digits(PYTHONINTMAXSTRDIGITS)

n, k, d = map(int, input().split())


def modulo(a, b, mod):
    res = 0
    a %= mod
    while b:
        if b & 1:
            res = (res + a) % mod
        a = (a * 2) % mod
        b >>= 1
    return res


def find_next_number(current_n, k):
    for i in range(0, 10):
        temp_n = current_n * 10 + i
        if modulo(temp_n, 1, k) == 0:
            return temp_n
    return -1


new_n = n

for j in range(d):
    current_modulo = modulo(new_n, 1, k)

    if current_modulo == 0:
        new_n *= 10
    else:
        new_n = find_next_number(new_n, k)

    if current_modulo == 0 and new_n % 10 == 0:
        new_n = new_n * (10 ** (d - j - 1))
        break

    if new_n == -1:
        break

print(new_n)
