"""D. Повторяющееся число"""

n, k = map(int, input().split())
a = list(map(int, input().split()))


def find_repeating_number(a, k):
    last_seen = {}
    for i, num in enumerate(a):
        if num in last_seen and i - last_seen[num] <= k:
            return True
        last_seen[num] = i
    return False


print("YES" if find_repeating_number(a, k) else "NO")

