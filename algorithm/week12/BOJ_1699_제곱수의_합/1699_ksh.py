from math import sqrt

N = int(input())
dp = list(range(N+1))

for i in range(1, N+1):
    for j in range(1, int(sqrt(i))+1):
        dp[i] = min(dp[i], dp[i - j**2] + 1)

print(dp[N])