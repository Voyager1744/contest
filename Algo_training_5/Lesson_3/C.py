"""C. Удаление чисел"""
n = int(input())
arr = list(map(int, input().split()))

element_count = {}
for num in arr:
    element_count[num] = element_count.get(num, 0) + 1

uniq_names = sorted(element_count.keys())

if len(uniq_names) < 2:
    print(0)
    exit()

max_len = 1
prev = uniq_names[0]
for i in range(1, len(uniq_names)):
    current = uniq_names[i]
    if abs(current - prev) <= 1:
        max_len = max(max_len, element_count[current] + element_count[prev])
    prev = current

print(len(arr) - max_len)
