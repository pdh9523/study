import sys

input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]


def rotate(cnt) :  # rotate 함수 설정 : 반복 수를 인자로 받아서 cnt 수만큼 반복
    global arr
    for _ in range(cnt):
        tmp = [[0]*M for _ in range(N)]
        for idx in range(min(N,M)//2+1):
            dr = 0
            i,j = idx,idx
            while dr != 4:
                di = i + dx[dr]
                dj = j + dy[dr]
                if 0 <= di < N and 0 <= dj < M and tmp[di][dj] == 0:
                    tmp[di][dj] = arr[i][j]
                    i,j=di,dj
                else :
                    dr+=1
        arr = [row[:] for row in tmp]           # 깊은 복사
    return tmp





N,M,R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

a = rotate(R)

for b in a:
    print(*b)

# 로테이션마다 깊은 복사를 반복해서 성능이 낮음