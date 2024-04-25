'21:18 ~ 21:48'

N = int(input())

if N < 4:
    dp = ['SK', 'CY', 'SK', 'SK']
    print(dp[N-1])
else:
    dp = ['SK'] * N   # 남은 돌의 개수별로 누가 이기는지 담는다.
    dp[1] = 'CY'
    for i in range(4, N):
        can = [1, 3, 4]
        if dp[i-1] == 'CY' or dp[i-3] == 'CY' or dp[i-4] == 'CY':
            pass
        else:
            dp[i] = 'CY'
    print(dp[N-1])