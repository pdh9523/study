d = 10**9+7

N,M = map(int,input().split())
DP = [ [0] * M for _ in range(N) ] 

# 초기값 설정
for i in range(N) : DP[i][0] = 1
for j in range(M) : DP[0][j] = 1

# 올 수 있는 이전 좌표들의 값을 합산하면서 리스트를 순회
for i in range(1,N):
    for j in range(1,M):
        DP[i][j] = (DP[i-1][j] + DP[i][j-1] + DP[i-1][j-1])%d
# 출력
print(DP[-1][-1]%d)