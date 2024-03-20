"""Плейлисты"""
n = int(input())

res_set = set()

for i in range(n):
    k = int(input())
    current_set = set(input().split())
    if not res_set:
        res_set = current_set
    else:
        res_set = res_set.intersection(current_set)

print(len(res_set))
print(*sorted(res_set))
