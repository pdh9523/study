'** visited 출발 지점 표시해주기 **'

'''
집까지 가는 모든 경우의 수를 구한다.
거리가 K인 경우를 cnt 한다.
거리가 K가 되었는데 집이 아니라면 종료

출발지점 : [R-1, 0] | 도착지점 : [0, C-1]
'''

def comebackhome(i, j, dist):
    global cnt

    if dist == K:
        if [i, j] == [0, C-1]:
            cnt += 1
        return

    for k in range(4):
        p, q = i + di[k][0], j + di[k][1]
        if 0 <= p < R and 0 <= q < C:
            if data[p][q] == '.' and visited[p][q] == 0:
                visited[p][q] = 1
                comebackhome(p, q, dist+1)
                visited[p][q] = 0


R, C, K = map(int, input().split())
data = [list(input()) for _ in range(R)]

di = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = [[0] * C for _ in range(R)]
visited[R-1][0] = 1
cnt = 0

if K >= R + C - 1:
    comebackhome(R-1, 0, 1)

print(cnt)