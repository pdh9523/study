import sys
sys.setrecursionlimit(100000)

def dfs(x, y, height):
    if x < 0 or x >= n or y < 0 or y >= n: # 좌표가 행렬 밖이라면
        return False
    if visited[x][y] or arr_height[x][y] <= height: # 높이가 낮다면
        return False
    visited[x][y] = True # 위 조건을 뚫었다면 True로 변경
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]: # 4방향 탐색
        nx, ny = x + dx, y + dy
        dfs(nx, ny, height) # 똑같이 조사
    return True

n = int(input())
arr_height = [list(map(int, input().split())) for _ in range(n)]
max_height = max(max(row) for row in arr_height) # 제일 큰 높이를 찾아야함

answer = 0 # 최종 결과
for height in range(max_height):
    visited = [[False] * n for _ in range(n)] # 방문기록용 
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr_height[i][j] > height: # 도착안했고, 높다면
                dfs(i, j, height)
                cnt += 1
    answer = max(answer, cnt)

print(answer)
