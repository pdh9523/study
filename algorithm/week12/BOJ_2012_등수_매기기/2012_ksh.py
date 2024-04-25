'20:47 ~ 20:52'

import sys
input = sys.stdin.readline

N = int(input())
expectation = [int(input()) for _ in range(N)]   # 예상 등수

expectation.sort()

result = 0
for i in range(N):
    result += abs(i+1 - expectation[i])

print(result)