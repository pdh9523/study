from collections import deque


N,M = map(int,input().split())
q = deque(range(1,N+1))
target = [*map(int,input().split())]
cnt = 0

for i in target :
    while q[0] != i :
        # 인덱스가 중앙보다 왼쪽에 있으면
        if q.index(i) <= len(q)//2:
            # 반시계
            rot=-1
        else :
            # 아니면 시계
            rot=1
        # 방향으로 돌림
        q.rotate(rot)
        cnt += 1
    # 다 돌렸으면 팝
    q.popleft()
    
print(cnt)