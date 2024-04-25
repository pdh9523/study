dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]
for i in range(21):
    for j in range(21):
        for k in range(21):
            if dp[i][j][k] == 0:
                if i*j*k == 0:
                    dp[i][j][k] = 1
                elif i < j < k:
                    dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
                else:
                    dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]


while 1:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break

    print(f'w({a}, {b}, {c}) = ', end='')
    if a <= 0 or b <= 0 or c <= 0:
        print(dp[0][0][0])
    elif a > 20 or b > 20 or c > 20:
        print(dp[20][20][20])
    else:
        print(dp[a][b][c])