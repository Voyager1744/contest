"""Продавец рыбы"""


N, K = map(int, input().split())
prices = list(map(int, input().split()))

max_profit = 0
min_price = float('inf')

for i in range(N):
    min_price = min(min_price, prices[i])

    for j in range(i + 1, min(N, i + K + 1)):
        profit = prices[j] - prices[i]
        if profit > max_profit:
            max_profit = profit

print(max_profit)



"""
5 2
1 2 3 4 5

5 2
5 4 3 2 1


"""