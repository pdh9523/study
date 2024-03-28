import sys
from collections import deque


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(N, M, K, maze):
    # K까지 써서 배열확인
    visited = [[[False] * (K + 1) for _ in range(M)] for _ in range(N)]
    
    queue = deque([(0, 0, 1, 0)])  # x, y, 이동거리, 벽뿌
    visited[0][0][0] = True

    while queue:
        x, y, dist, wall_break = queue.popleft()

        # 도착지
        if x == N - 1 and y == M - 1:
            return dist

        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            
            if 0 <= nx < N and 0 <= ny < M:
                # 길
                if maze[nx][ny] == 0:
                    if not visited[nx][ny][wall_break]:
                        visited[nx][ny][wall_break] = True
                        queue.append((nx, ny, dist + 1, wall_break))
                # 벽
                else:
                    # 벽뿌 카운트 쌓기
                    if wall_break < K and not visited[nx][ny][wall_break + 1]:
                        visited[nx][ny][wall_break + 1] = True
                        queue.append((nx, ny, dist + 1, wall_break + 1))

    # 위에꺼 다했음... 못가는거임
    return -1

N, M, K = map(int, sys.stdin.readline().strip().split()) # 행렬 및 벽 부수기
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)] # 미로
result = bfs(N, M, K, maze)
print(result)