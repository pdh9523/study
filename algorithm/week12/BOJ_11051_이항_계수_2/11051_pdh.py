N,K = map(int,input().split())

DP = [1,1]
for i in range(2,N+1) :
    DP.append((i*DP[-1]))
# nCk
print((DP[N] // DP[K] // DP[N-K])%10007)