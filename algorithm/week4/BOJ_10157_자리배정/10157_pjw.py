C, R = map(int, input().split()) # 공연장 격자 크기 C = 가로, R = 세로
K = int(input()) # 대기번호

# 이거 스네일 아닌가여? 개꿀

dx = [-1, 0, 1, 0] # 방향 정해져있어서
dy = [0, 1, 0, -1] # 임의로 수정하면 안되여

arr = [[0]*C for _ in range(R)]
count = 1
x, y = R-1, 0
dir = 0
arr[x][y] = count
tar_i = 0
tar_j = 0
while count < C * R:
    nx = x + dx[dir]
    ny = y + dy[dir]

    if 0 <= nx < R and  0 <= ny < C and arr[nx][ny] == 0:
        count += 1
        arr[nx][ny] = count
        x, y = nx, ny
    else:
        dir += 1
        if dir >= 4:
            dir = 0
    
for i in range(R):
    for j in range(C):
        if arr[i][j] == K:
            tar_i = i
            tar_j = j


if K > C * R or K <= 0:
    print(0)
else:
    real_i = 1 + tar_j
    real_j = R - tar_i  

    print(real_i, real_j)