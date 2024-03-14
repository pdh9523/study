from collections import deque


def ripe_tomato():
    global max_day

    while q:
        k, i, j = q.popleft()
        for z in range(6):  # 6방향을 순회하며
            if 0 <= k + dk[z] < H and 0 <= i + di[z] < N and 0 <= j + dj[z] < M:  # 범위 내에서
                if tomato[k + dk[z]][i + di[z]][j + dj[z]] == 0:                  # 1. 익지 않은 토마토라면,
                    tomato[k + dk[z]][i + di[z]][j + dj[z]] = 1                   # 토마토를 익혀준다.
                    day[k + dk[z]][i + di[z]][j + dj[z]] = day[k][i][j] + 1       # 해당 토마토가 익는데 소요된 기간을 표시한다.
                    if max_day < day[k + dk[z]][i + di[z]][j + dj[z]]:
                        max_day = day[k + dk[z]][i + di[z]][j + dj[z]]
                    q.append([k + dk[z], i + di[z], j + dj[z]])


M, N, H = map(int, input().split())                                      # 상자의 크기 가로 M, 세로 N, 쌓아 올려지는 상자의 수 H
tomato = []
for h in range(H):                                                       # H개의 상자에 대하여 토마토 정보 담기
    tomato.append([list(map(int, input().split())) for _ in range(N)])   # 1 : 익은 토마토, 0 : 익지 않은 토마토, -1 : 빈칸

di = [1, -1, 0, 0, 0, 0]
dj = [0, 0, 1, -1, 0, 0]
dk = [0, 0, 0, 0, 1, -1]

day = [[[0] * M for _ in range(N)] for _ in range(H)]
max_day = 0
q = deque()

for c in range(H):
    for a in range(N):
        for b in range(M):
            if tomato[c][a][b] == 1 and day[c][a][b] == 0:   # 익은 토마토이면서, 아직 확인하지 않은 토마토라면,
                q.append([c, a, b])                          # 작업 리스트 q 에 담기.
ripe_tomato()

for r in range(H):              # 상자들을 순회하며 토마토 확인
    for p in range(N):
        if 0 in tomato[r][p]:   # 안 익은 토마토가 있다면,
            print(-1)           # 결과 -1 출력
            exit()
else:                           # 안 익은 토마토가 없다면,
    print(max_day)