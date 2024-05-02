'09:10 ~ 09:27'

import sys
input = sys.stdin.readline

N = int(input())
answer = [int(input()) for _ in range(N)]

max_cnt, best = 0, 0
for i in range(N):
    k = answer[i] - 1
    visited = [0] * N
    visited[i] = 1
    cnt = 0
    while visited[k] == 0:
        visited[k] = 1
        k = answer[k] - 1
        cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
        best = i + 1

print(best)