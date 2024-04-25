import math

N = int(input())  # 자연수

# dp 배열 초기화
dp = [0] * (N + 1)

# dp 배열 채우기
for i in range(1, N + 1):
    dp[i] = dp[i - 1] + 1

    # 제곱수인 경우
    for j in range(1, int(math.sqrt(i)) + 1):
        square = j * j
        if square <= i:
            dp[i] = min(dp[i], dp[i - square] + 1)

print(dp[N])

# 따로 alpha 만들어서 제곱수 집어넣고 하면 시간초과뜸... 바로 넣어야댐
