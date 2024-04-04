N = int(input()) # 일 수
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    day, money = arr[i][0], arr[i][1]
    end_day = day + i

    if end_day > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(money+dp[end_day], dp[i+1])

print(max(dp))