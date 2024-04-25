N, K = map(int, input().split()) # 이 항 계 수

result1 = 1
for i in range(1,N+1):
    result1 *= i

result2 = 1
for i in range(1, K+1):
    result2 *= i

result3 = 1
for i in range(1, (N-K)+1):
    result3 *= i

result = (result1//(result2*result3))%10007
print(int(result))