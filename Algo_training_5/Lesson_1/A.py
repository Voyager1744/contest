"""Покраска деревьев"""

p, v = list(map(int, input().split()))
m, q = list(map(int, input().split()))

start_p = p - v
end_p = p + v
count_p = end_p - start_p + 1

start_m = m - q
end_m = m + q
count_m = end_m - start_m + 1

print(start_p, end_p, count_p)
print(start_m, end_m, count_m)


def count_der(sp, ep, sm, em, cp, cm):
    res = 0
    if sp == sm:
        res = max([cp, cm])
    elif sp < sm < ep < em:
        res = sum([cp, cm]) - (ep - sm) - 1
    elif sp < sm < em < ep:
        res = cp
    elif sp < ep == sm and sm < em:
        res = sum([cp, cm]) - 1
    elif sp < ep < sm < em:
        res = sum([cp, cm])

    return res


if start_p < start_m:
    print(count_der(start_p, end_p,start_m, end_m, count_p, count_m))
else:
    print(count_der(start_m, end_m, start_p, end_p, count_m, count_p))
