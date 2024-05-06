from heapq import heappush, heappop
import sys


input = sys.stdin.readline

N,H,T = map(int,input().split())

hq = [ ]
for _ in range(N):
    # 최대힙 구성
    heappush(hq, -int(input()))

# check = True -> 자기가 키가 가장 큰게 아니다 
check = True
for i in range(T+1):
    # 검증 
    # 체크 
    if check and -hq[0] < H :
        print("YES")
        print(i)
        check = False
        
    # i 가 마지막인 경우 NO 출력

    if check and i == T:
        print("NO")
        print(-hq[0])
        break
    


    target = -heappop(hq)

    if target != 1 :
        target //=2
    
    heappush(hq,-target)