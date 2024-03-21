"""E. Амбициозная улитка"""

n = int(input())
maxgoodi = -1
maxbadi = -1
a = []
b = []
used = [False] * (n + 1)
for i in range(n):
    ta, tb = map(int, input().split())
    a.append(ta)
    b.append(tb)
    if ta >= tb and (maxgoodi == -1 or tb > b[maxgoodi]):
        maxgoodi = i
    if ta < tb and (maxbadi == -1 or ta > a[maxbadi]):
        maxbadi = i
ans = []
maxh = 0
for i in range(n):
    if a[i] > b[i] and i != maxgoodi:
        ans.append(i + 1)
        used[i + 1] = True
        maxh += a[i] - b[i]

if maxgoodi != -1 and \
        (maxbadi != -1 and a[maxgoodi] > a[maxgoodi] - b[maxgoodi] + a[maxbadi]) or \
        (maxbadi == -1):
    maxh += a[maxgoodi]
    ans.append(maxgoodi + 1)
    used[maxgoodi + 1] = True
else:
    if maxbadi != -1:
        if maxgoodi != -1:
            maxh += a[maxgoodi] - b [maxgoodi]
            ans.append(maxgoodi + 1)
            used[maxgoodi + 1] = True
        maxh += a[maxbadi]
        ans.append(maxbadi + 1)
        used[maxbadi + 1] = True
print(maxh)
for i in range(1, n + 1):
    if not used[i]:
        ans.append(i)
print(*ans)
