"""
1*k + 2*(k-1) + 3*(k-2) + ...+ (k-1)*(k-(k-2)) + k*(k-(k-1))

k = 5

1*1*5 + 2*1*4 + 3*1*3 + 4*1*2 + 5*1*1
сумма = 5 + 8 + 9 + 8 + 5 = 33

k = 2

1*1*2 + 2*1*1
сумма = 4

k = 6

1*1*6 + 2*1*5 + 3*1*4 + 4*1*3 + 5*1*2 + 6*1*1

сумма = 6 + 10 + 12 + 12 + 10 + 6 = 56


next member = n*(k-(n-1))

k = 2
p1 = 1*(2-(1-1)) = 2
p2 = 2*(2-(2-1)) = 2

k = 3
p1 = 1*(3-(1-1)) = 3
p2 = 2*(3-(2-1)) = 4
p3 = 3*(3-(3-1)) = 3

"""


def summa_pos(k):
    res = 0
    for i in range(1, k + 1):
        nextnum = i * (k - (i - 1))
        res += nextnum
    return res


def count_pos(k):
    return summa_pos(k) + k


def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l - 1


def check(m, checkparams):
    q = checkparams
    x = count_pos(m)
    return x >= q


n = int(input())
if n == 0:
    print(0)
    exit()
# if n <= 6:
#     print(1)
#     exit()
else:
    print(lbinsearch(0, n, check, n))
