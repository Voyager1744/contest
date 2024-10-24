t = int(input())
for test in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    prevebrake = 0
    curmin = a[0]
    ans = []
    for i in range(n):
        curmin = min(curmin, a[i])
        if prevebrake + curmin <= i:
            ans.append(i - prevebrake)
            prevebrake = i
            curmin = a[i]
    ans.append(n - prevebrake)
    print(len(ans))
    print(*ans)
