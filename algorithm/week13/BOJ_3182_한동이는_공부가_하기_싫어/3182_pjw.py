from collections import deque

N = int(input()) # 1~N까지
alpha = [int(input()) for _ in range(N)] # N줄에 걸쳐 숫자가 주어짐

def bfs(alpha, start):
    visited = [False] * (N+1)
    queue = deque([start])
    visited[start] = True
    count = 0
    
    while queue:
        cur = queue.popleft()
        count += 1
        
        next_al = alpha[cur - 1]
        if not visited[next_al]:
            visited[next_al] = True
            queue.append(next_al)
            
    return count

max_count = -1
max_senior = -1

for i in range(1, N+1):
    count = bfs(alpha, i)
    if count > max_count:
        max_count = count
        max_senior = i

print(max_senior)