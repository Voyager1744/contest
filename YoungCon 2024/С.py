MOD = 10 ** 9 + 7


def count_partitions(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(n, i - 1, -1):
            dp[j] = (dp[j] + dp[j - i]) % MOD

    return dp[n]


def distinct_parties(n):
    if n == 1:
        return 1

    total = 0
    for i in range(1, n + 1):
        total = (total + count_partitions(n - 1)) % MOD

    return total


# Reading input
n = int(input().strip())

# Output the result
print(distinct_parties(n))
