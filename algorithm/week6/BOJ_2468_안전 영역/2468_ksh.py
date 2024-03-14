def bfs():
    while queue:
        y, x = queue.pop()
        for k in range(4):
            if 0 <= y + di[k] < N and 0 <= x + dj[k] < N:
                if visited[y + di[k]][x + dj[k]] == 0 and after_rain[y + di[k]][x + dj[k]] == 1:
                    visited[y + di[k]][x + dj[k]] = 1
                    queue.append([y + di[k], x + dj[k]])

N = int(input())   # 2차원 배열의 크기
area = [list(map(int, input().split())) for _ in range(N)]   # 어떤 지역의 높이 정보
# 델타 탐색, bfs, 잠기지 않고 이어져 있는 영역 개수 구하기

lowest = 100
highest = 1
for i in range(N):
    for j in range(N):
        if area[i][j] < lowest:
            lowest = area[i][j]
        if area[i][j] > highest:
            highest = area[i][j]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

max_cnt = 0

for rain in range(lowest-1, highest):          # 지역의 높이 중 가장 낮은 지역 -1, 가장 높은 지역 -1 까지의 범위 내에서 장마철 구하기
    after_rain = [[0] * N for _ in range(N)]   # 잠기면 0, 안잠기면 1
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] > rain:
                after_rain[i][j] = 1
    for p in range(N):
        for q in range(N):
            if visited[p][q] == 0 and after_rain[p][q] == 1:
                cnt += 1
                queue = [[p, q]]
                bfs()
    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)