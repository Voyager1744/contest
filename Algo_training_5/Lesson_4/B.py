"""B. Одномерный морской бой"""
def summa_pos(k):
    res = k*(k+1)*(k+2)//6
    c = (k * (k + 1) // 2) - 1

    return res + c



def rbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, checkparams):
            l = m
        else:
            r = m - 1
    return l


def check(m, checkparams):
    q = checkparams
    x = summa_pos(m)
    return x <= q


n = int(input())
if n == 0:
    print(0)
    exit()
if n < 6:
    print(1)
    exit()
else:
    print(rbinsearch(2, n, check, n))
