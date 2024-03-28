"""A. Быстрый поиск в массиве"""

def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l


def rbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, checkparams):
            l = m
        else:
            r = m - 1
    return l


def check_l(m, checkparams):
    seq, x = checkparams
    return seq[m] >= x


def check_r(m, checkparams):
    seq, x = checkparams
    if m >= len(seq):
        return False
    return seq[m] <= x


n = int(input())
a = list(map(int, input().split()))
a.sort()
k = int(input())
ans = []


def find_count_num(a, l, r):
    if l > a[-1]:
        find_l = -1
    else:
        find_l = lbinsearch(0, n, check_l, (a, l))
    if r < a[0]:
        find_r = -1
    else:
        find_r = rbinsearch(0, n, check_r, (a, r))
    if find_r < find_l or find_l == -1 or find_r == -1:
        return 0
    return find_r - find_l + 1



for _ in range(k):
    l, r = map(int, input().split())
    ans.append((find_count_num(a, l, r)))

print(*ans)


"""
5
10 1 10 3 4
4
1 10
2 9
3 4
2 2

"""