N = int(input())
DP = [float('inf')] * (N+1)
sqr = []
# 제곱 수 구해서 sqr 에 담기
for i in range(1,N+1):
    if i ** 2 <= N :
        sqr.append(i**2)
        DP[i**2] = 1        # 제곱 수 자리의 DP 값은 1로
    else :                  # i**2 가 목표 N값을 넘었을 경우 break
        break

for i in range(1,N+1):
    for num in sqr :
        if i + num < N+1 :
            DP[i+num] = min(DP[i+num],DP[i]+1)  # DP
print(DP[-1])