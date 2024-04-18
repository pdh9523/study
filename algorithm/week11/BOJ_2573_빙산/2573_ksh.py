import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())   # 행, 열
ocean = [list(map(int, input().split())) for _ in range(N)]
year = 0

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

while 1:
    year += 1
    melted_ocean = [[0] * M for _ in range(N)]
    ice = 0

    for i in range(1, N-1):
        for j in range(1, M-1):
            if ocean[i][j] > 0:
                ice += 1
                for k in range(4):
                    if ocean[i+di[k]][j+dj[k]] == 0:
                        melted_ocean[i][j] += 1

    if ice == 0:
        exit(print(0))

    for i in range(1, N-1):
        for j in range(1, M-1):
            if melted_ocean[i][j] > 0:
                ocean[i][j] -= melted_ocean[i][j]
                if ocean[i][j] < 0:
                    ocean[i][j] = 0

    queue = deque([])
    visited = [[True] * M for _ in range(N)]
    cnt = 0

    for i in range(1, N-1):
        for j in range(1, M-1):
            if ocean[i][j] > 0 and visited[i][j]:
                queue.append([i, j])
                cnt += 1
                if cnt > 1:
                    exit(print(year))
                while queue:
                    p, q = queue.popleft()
                    for k in range(4):
                        y, x = p+di[k], q+dj[k]
                        if ocean[y][x] > 0 and visited[y][x]:
                            queue.append([y, x])
                            visited[y][x] = False