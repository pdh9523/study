# 행렬은 1~N까지임 
# 파이프는 2개의 연속된 칸을 차지하며, 가로, 세로, 대각선 방향이 가능하다.
# 파이프는 벽을 긁으면 안된다.
# 파이프는 1,1 1,2 에서 시작하며, 한쪽끝을 N,N으로 이동시키는 방법의 개수를 구하자

N = int(input()) # 집의 크기
arr = [list(map(int, input().split())) for _ in range(N)] # 빈칸 0, 벽 1

dp = [[[0]*3 for _ in range(N)] for _ in range(N)] # 3차원 dp
dp[0][1][0] = 1 # 0,1위치에 가로 방향 파이프, i, j, 방향 0가로 1세로 2대각

for i in range(N):
    for j in range(2, N):
        if arr[i][j] == 1:
            continue
        
        # 가로
        dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]

        # 세로
        dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]

        # 대각선
        if arr[i-1][j] == 0 and arr[i][j-1] == 0 and arr[i-1][j-1] == 0:
            dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

print(sum(dp[N-1][N-1]))