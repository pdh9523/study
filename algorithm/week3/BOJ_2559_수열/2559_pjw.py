import sys
sys.stdin = open('input.txt')

# 시간초과 떠요 ㅈ같아요 시간초과는 platinum부터라고 했으니깐 전 여기까지
N, K = map(int, input(). split())
arr = list(map(int, input().split()))

sum_K = []
result = 0
for i in range(N - K +1):
    for j in range(i, i + K):
        result += arr[j]
    sum_K.append(result)
    result = 0

alpha = max(sum_K)
print(alpha)