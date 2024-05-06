from collections import deque

N = int(input())
# q인지 stack인지
style = [*map(int,input().split())]
# 각각 원소 
elements = [*map(int,input().split())]

M = int(input())
# 삽입할 원소
new_elem = [*map(int,input().split())]

q = deque()

for i in range(N):
    # 스택은 볼 필요 없음 
    # 큐만 그냥 앞으로 더해주면 됨
    if style[i] == 0 :
        q.appendleft(elements[i])

# 큐에 마지막으로 합쳐주고
q.extend(new_elem)
# M만큼만 출력
print(*list(q)[:M])