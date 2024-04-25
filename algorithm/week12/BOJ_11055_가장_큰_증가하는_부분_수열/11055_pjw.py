# 증가하는 부분 수열 중 합이 가장 큰 것
N = int(input()) # 수열의 크기
arr = list(map(int, input().split())) # 수열
dp = [0] * N # 디피


for i in range(N):
    dp[i] = arr[i]
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))