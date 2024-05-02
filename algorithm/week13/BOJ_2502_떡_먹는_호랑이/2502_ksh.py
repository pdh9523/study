'17:00 - 17:10'

D, K = map(int, input().split())

while True:
    for i in range(1, K+1):
        for j in range(i, K+1):
            dp = [0] * (D+1)
            dp[1], dp[2] = i, j
            for d in range(3, D+1):
                dp[d] = dp[d-1] + dp[d-2]
            if dp[D] == K:
                print(i)
                print(j)
                exit()