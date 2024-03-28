import sys
input = sys.stdin.readline
from collections import deque

N, M, K = map(int, input().split())
land = [list(input().strip()) for _ in range(N)]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

queue = deque([[0, 0, 0]])   # i, j, b
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
s = float('inf')

while queue:
    i, j, b = queue.popleft()
    if visited[i][j][b] > s:
        continue

    if b <= K:
        for k in range(4):
            p, q = i + di[k], j + dj[k]
            if 0 <= p < N and 0 <= q < M:
                if land[p][q] == '0' and (visited[p][q][b] == 0 or visited[p][q][b] > visited[i][j][b] + 1):
                    visited[p][q][b] = visited[i][j][b] + 1
                    if p != N - 1 or q != M - 1:
                        queue.append([p, q, b])
                    else:
                        if visited[p][q][b] < s:
                            s = visited[p][q][b]

                elif land[p][q] == '1' and b < K and (visited[p][q][b] == 0 or visited[p][q][b] > visited[i][j][b] + 1):
                    visited[p][q][b+1] = visited[i][j][b] + 1
                    if p != N - 1 or q != M - 1:
                        queue.append([p, q, b+1])
                    else:
                        if visited[p][q][b+1] < s:
                            s = visited[p][q][b+1]

result = visited[N-1][M-1]

if result.count(0) == K+1:
    print(-1)
else:
    while 0 in result:
        result.pop(result.index(0))
    print(min(result))