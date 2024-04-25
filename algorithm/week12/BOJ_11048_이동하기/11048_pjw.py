# 얘도 dp네 ㅋㅋ
N, M = map(int, input().split()) # 미로 크기
arr = [list(map(int, input().split())) for _ in range(N)] # 사탕개수
dp = [[0] * M for _ in range(N)] # 2차원
dp[0][0] = arr[0][0]

for i in range(N):
    for j in range(M):
        if i-1 < 0:
            dp[i][j] = dp[i][j-1] + arr[i][j]
        elif j-1 < 0:
            dp[i][j] = dp[i-1][j] + arr[i][j]
        else:
            dp[i][j] = max(dp[i][j-1]+arr[i][j], dp[i-1][j]+arr[i][j], dp[i-1][j-1]+arr[i][j])

print(dp[N-1][M-1])