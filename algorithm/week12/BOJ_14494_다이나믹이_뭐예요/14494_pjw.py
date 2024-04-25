n, m = map(int, input().split()) # 행 렬
dp = [[0]*m for _ in range(n)] # 2차원 dp

for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i][j-1] + dp[i-1][j] + dp[i-1][j-1]) % 1000000007

print(dp[n-1][m-1])