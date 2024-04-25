N = int(input()) # 게임판 크기
arr = [list(map(int, input().split())) for _ in range(N)] # 판
dp = [[0]*N for _ in range(N)] # 2차원
dp[N-1][N-1] = 1

for i in range(N-1, -1, -1):
    for j in range(N-1, -1, -1):
        if i == N-1 and j == N-1:
            continue # 도착점임

        if j + arr[i][j] < N: # 안빗겨나감
            dp[i][j] += dp[i][j + arr[i][j]]

        if i + arr[i][j] < N:
            dp[i][j] += dp[i + arr[i][j]][j]

print(dp[0][0])