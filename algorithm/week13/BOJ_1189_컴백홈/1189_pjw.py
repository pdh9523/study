R, C, K = map(int, input().split())  # R과 C, K를 입력받습니다.

arr = []

for _ in range(R):
    row = list(input())
    arr.append(row)

dx = [0, -1,0,1]
dy = [1, 0,-1,0]
visited = [[False] * C for _ in range(R)]  # 방문기록

def dfs(arr, visited, start_x, start_y, length):

    if start_x == 0 and start_y == C-1: # 도착하고 거리가 K일 때
        if length == K:
            return 1
    
    visited[start_x][start_y] = True
    count = 0

    for k in range(4):
        nx = start_x + dx[k]
        ny = start_y + dy[k]
        if nx >= 0 and nx < R and ny >= 0 and ny < C and not visited[nx][ny] and arr[nx][ny] != 'T':
            count += dfs(arr, visited, nx, ny, length+1)
    
    visited[start_x][start_y] = False
    return count

print(dfs(arr, visited, R-1, 0, 1))
