"""F. Колесо Фортуны"""

n = int(input())
vals = list(map(int, input().split()))
a, b, k = map(int, input().split())

minsect = (a - 1) // k
maxsect = (b - 1) // k

ans = -1
for j in range(2):
    usedsect = [False] * n
    for i in range(minsect, maxsect + 1):
        ans = max(ans, vals[i % n])
        if usedsect[i % n]:
            break
        usedsect[i % n] = True
    vals = [vals[0]] + vals[1:][::-1]
print(ans)
