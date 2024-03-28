from collections import deque

# 이동할 네 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, n):
    distance = [[float('inf')] * n for _ in range(n)]
    distance[0][0] = graph[0][0]  # 시작 지점의 비용은 그대로
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()
        # 네 방향으로 이동하면서 최소 비용 갱신
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if distance[nx][ny] > distance[x][y] + graph[nx][ny]:
                    distance[nx][ny] = distance[x][y] + graph[nx][ny]
                    queue.append((nx, ny))

    return distance[n-1][n-1]


case = 1
while True:
    n = int(input())
    if n == 0:
        break
    
    cave = []
    for _ in range(n):
        cave.append(list(map(int, input().split())))
    
    result = bfs(cave, n)
    print("Problem {}: {}".format(case, result))
    case += 1


