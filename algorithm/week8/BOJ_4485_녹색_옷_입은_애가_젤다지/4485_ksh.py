import sys
input = sys.stdin.readline
from collections import deque

t = 0
while 1:
    t += 1
    N = int(input())   # 동굴의 크기 N
    if N == 0:
        break
    minus = [list(map(int, input().split())) for _ in range(N)]   # 도둑루피의 정보

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    queue = deque([[0, 0]])
    visited = [[-1] * N for _ in range(N)]
    visited[0][0] = minus[0][0]

    while queue:
        i, j = queue.popleft()
        for k in range(4):
            p, q = i+di[k], j+dj[k]
            if 0 <= p < N and 0 <= q < N:
                temp = visited[i][j] + minus[p][q]
                if visited[p][q] == -1 or visited[p][q] > temp:
                    visited[p][q] = temp
                    if p != N-1 or q != N-1:
                        queue.append([p, q])

    print(f'Problem {t}: {minus[N-1][N-1] + min(visited[N-2][N-1], visited[N-1][N-2])}')