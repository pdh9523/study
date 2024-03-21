# 돈을 최대한 많이 지불해서 카드를 N개 구매
# 갯수가 적어도 비싸면 높은 등급의 카드가 많을 것이라고 생각 => 비싼거 위주로 삼
N = int(input()) # 구매할 카드 개수
P_i = list(map(int, input().split())) # 1~N개 들어있는 카드팩 가격
P_i.insert(0,0) # 0번이 없으니까 넣자
dp = [0] * (N + 1)  # DP 

for i in range(1, N + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + P_i[j]) # i번째 DP는 저거 중에 하나임

print(dp[N])
