n = int(input()) # 타깃 자연수

# 223의 제곱까지가 5만이 안됨

dp = [0] + [float('inf')] * (n+1)
alpha = []
for double in range(1, 224):
    alpha.append(double*double)

for betta in alpha:
    for i in range(betta, n+1):
        dp[i] = min(dp[i], dp[i - betta] + 1)

print(dp[n])