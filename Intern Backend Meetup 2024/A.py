def can_win_game(a, b, c):

    if (a == 0 and b == 1 and c == 0) or \
       (a == 0 and b == 0 and c == 1) or \
       (a == 1 and b == 0 and c == 0) or \
       (a % 2 == 0 and b % 2 == 0 and b != 0 and (a + b) // 2 - c == 1) or \
       (a % 2 == 0 and c % 2 == 0 and c != 0 and (a + c) // 2 - b == 1) or \
       (b % 2 == 0 and c % 2 == 0 and c != 0 and (b + c) // 2 - a == 1):
        return "Yes"
    else:
        return "No"

n = int(input())

for _ in range(n):
    a, b, c = map(int, input().split())
    print(can_win_game(a, b, c))
