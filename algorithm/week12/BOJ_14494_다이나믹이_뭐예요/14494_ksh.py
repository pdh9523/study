'09:40 ~ 09:52'

N, M = map(int, input().split())

dp = [[0] * (M+1) for _ in range(N+1)]
dp[1][1] = 1
for i in range(1, N+1):
    for j in range(1, M+1):
        if i == 1 and j == 1:
            pass
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] + dp[i][j-1]) % 1000000007

print(dp[N][M])