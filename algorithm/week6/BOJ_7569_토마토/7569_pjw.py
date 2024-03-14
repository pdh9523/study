from collections import deque

def bfs(queue): # bfs 써야됨
    days = -1  # 시작일부터 1일이 지나야 하므로 -1로 초기화
    while queue:
        days += 1 # 1일씩 올리면서
        for _ in range(len(queue)): # 큐의 길이만큼
            x, y, z = queue.popleft() # 팝해줄거임
            for dx, dy, dz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]: # 상하좌우전후
                nx, ny, nz = x + dx, y + dy, z + dz
                if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and tomato_boxes[nz][nx][ny] == 0:
                    # 세 가지 좌표가 범위 안이고 익지 않았다면
                    tomato_boxes[nz][nx][ny] = 1 # 익었음
                    queue.append((nx, ny, nz)) # queue에 넣는다.
    return days # 몇 일만에 익는지 검사할꺼니까

M, N, H = map(int, input().split())  # 상자의 크기 입력 가로 세로 높이
tomato_boxes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]  # 토마토

queue = deque([])
for z in range(H): # 높이
    for x in range(N): # 세로
        for y in range(M): # 가로
            if tomato_boxes[z][x][y] == 1:
                queue.append((x, y, z))

days = bfs(queue)

for boxes in tomato_boxes:
    for row in boxes:
        if 0 in row:
            print(-1)
            exit()

print(days)
            