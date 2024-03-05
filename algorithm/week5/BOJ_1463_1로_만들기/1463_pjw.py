N = int(input())

dp = [0] * (N+1) # 디피를 씁시다

for i in range(2, N + 1):
    dp[i] = dp[i-1] + 1 # 한개 씩 증가 시키면서
    # 조건은 유동적으로 하면 된다능
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1) # 원래 꺼랑, 자기//2 한거에 1더한거랑 비교
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1) # 원래 꺼랑, 자기//3 한거에 1더한거랑 비교
# 카운트 출력~
print(dp[N])