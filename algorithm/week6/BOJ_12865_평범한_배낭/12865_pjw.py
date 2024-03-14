def knapsack(N, K, weights, values):
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, K + 1):
            if weights[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])

    return dp[N][K]


N, K = map(int, input().split()) # 물건 갯수, 버티는 무게
weights = []
values = []

for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w) # 무게
    values.append(v) # 가치

print(knapsack(N, K, weights, values))
