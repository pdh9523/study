'Total 1H 38M | 09:53 ~ 10:49 (-4), 15:55 ~ 16:41'

N = int(input())                        # 수열의 크기
arr = list(map(int, input().split()))   # 수열

dp = [0] * (max(arr) + 1)
dp[arr[0]] = arr[0]
for i in range(1, N):
    dp[arr[i]] = max(dp[arr[i]], max(dp[:arr[i]]) + arr[i])

print(max(dp))

'''
10
7 9 38 6 47 96 156 5 96 47
=> 353
'''