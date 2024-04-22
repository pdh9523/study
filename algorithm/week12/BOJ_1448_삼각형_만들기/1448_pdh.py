import sys
from heapq import heappop, heappush


input = sys.stdin.readline

N = int(input())
hq = []

for _ in range(N):
    heappush(hq,-int(input()))      # 최대 힙 구성

c = -heappop(hq)
b = -heappop(hq)
a = -heappop(hq)

# 삼각형 조건 (큰 변의 길이 < 나머지 두 변의 길이)
while c >= a+b :
    b,c = a,b
    
    if not hq :
        exit(print(-1))
    a = -heappop(hq)

print(a+b+c)