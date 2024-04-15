from collections import deque 

dx = [1,0,-1,0]
dy = [0,1,0,-1]

N,M = map(int,input().split())

glacier = []

target = set()

for _ in range(N):
    ice = list(map(int,input().split()))
    target.update(ice)
    glacier.append(ice)


ans = 0
year = -1                                  # while 시작하면서 0 년으로 시작해야 하니까 -1년부터 시작
while True : 
    year += 1
    cnt = 0                                             # 빙산 개수
    visit = [[0]*M for _ in range(N)]                   # 전체에 대한 bfs로 빙산을 나눔
    for i in range(N):
        for j in range(M):
            
            if glacier[i][j] > 0 and not visit[i][j]:   
                q = deque([(i,j)])
                visit[i][j] = 1
                
                while q :
                    
                    x,y = q.popleft()

                    for dt in range(4):
                        di = x + dx[dt]
                        dj = y + dy[dt]
                    
                        if 0 <= di < N and 0 <= dj < M :
                            if not visit[di][dj] and glacier[di][dj] > 0 :
                                visit[di][dj] = 1
                                q.append((di,dj))
                cnt += 1

    if ans != cnt:                          # cnt와 ans가 다르다 (변했을 시 중단)
        if ans == 0 :                       # ans == 0 이었으면 초기조건 설정한 것이니 다시 넘어감
            ans = cnt               
        elif cnt == 0 :                     # cnt == 0 이면 0
            exit(print(0))
        elif ans != cnt :                   # ans가 0이 아닌 상태에서도 다르다면 변화가 일어난 것이므로
            exit(print(year))               # 탈출
        
    iceberg = [row[:] for row in glacier]   # 깊은 복사를 통해 임시적으로 참조할 대상을 만들어둠 
    for p in range(N):
        for q in range(M):
            for dt in range(4):
                dp = p + dx[dt]
                dq = q + dy[dt]
                if 0 <= dp < N and 0 <= dq < M :
                    if iceberg[dp][dq] == 0 and iceberg[p][q] !=0:
                        if glacier[p][q] >0:
                            glacier[p][q] -=1           # 주변에 0이 있는 경우 값을 1씩 내림 