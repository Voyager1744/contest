"""E. Два из трех"""

n1 = int(input())
a1 = set(map(int, input().split()))
n2 = int(input())
a2 = set(map(int, input().split()))
n3 = int(input())
a3 = set(map(int, input().split()))

res1 = set(a1) & set(a3)
res2 = set(a2) & set(a3)
res3 = set(a1) & set(a2)
result = sorted((list(res1 | res2 | res3)))
print(*result)
