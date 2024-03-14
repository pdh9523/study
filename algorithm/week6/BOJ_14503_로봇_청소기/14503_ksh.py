N, M = map(int, input().split())
r, c, d = map(int, input().split())   # 0 : 북, 1 : 동, 2 : 남, 3 : 서
room = [list(map(int, input().split())) for _ in range(N)]   # 0 : 청소되지 않은 빈 칸, 1 : 벽이 있음

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
cnt = 0

while 1:
    if room[r][c] == 0:
        room[r][c] = 2
        cnt += 1
    if room[r+1][c] != 0 and room[r-1][c] != 0 and room[r][c+1] != 0 and room[r][c-1] != 0:
        if room[r + di[d-2]][c + dj[d-2]] == 1:
            break
        else:
            r += di[d-2]
            c += dj[d-2]
    else:
        if d == 0:
            d = 3
        else:
            d -= 1
        if 0 <= r + di[d] < N and 0 <= c + dj[d] < M:
            if room[r + di[d]][c + dj[d]] == 0:
                r += di[d]
                c += dj[d]

print(cnt)