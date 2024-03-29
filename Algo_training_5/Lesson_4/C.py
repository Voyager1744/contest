n, m = tuple(map(int, input().split()))
polks = list(map(int, input().split()))



psum = [0] * (n + 1)
for i in range(n):
    psum[i + 1] = polks[i] + psum[i]


def make_psum(arr, n):
    psum = [0] * (n + 1)
    for i in range(n):
        psum[i + 1] = polks[i] + psum[i]
    return psum


def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l

def check(m, checkparams):
    s, arr, l = checkparams
    return arr[m + l] - 1 - arr[m] >= s

p_sum = make_psum(polks, n)


for _ in range(m):
    l, s = tuple(map(int, input().split()))
    
    polk = lbinsearch(0, len(p_sum) - l, check, (s, p_sum, l)) - 1

    count = p_sum[polk + l] - p_sum[polk]

    if polk >= len(p_sum) or count != s:
        print(-1)
    else:
        print(polk + 1)


"""
5 3
1 3 5 7 9
2 4
1 3
3 21

"""