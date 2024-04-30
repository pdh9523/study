dr = (0,1),(1,0),(0,-1),(-1,0)

def DFS(i,j,cnt=1):
    global ans
    # 집에 도착했는데
    if i==0 and j == M-1 :
        # 원하는 특정 거리면
        if cnt == K:
            ans += 1
            return 
    
    for dx,dy in dr :
       di,dj = i+dx, j+dy
       if 0<=di<N and 0<=dj<M:
          if visit[di][dj] : continue
          if arr[di][dj] == "T" : continue

          visit[di][dj] = 1
          DFS(di,dj,cnt+1)
          visit[di][dj] = 0


N,M,K = map(int,input().split()) # N:가로, M:세로, K:거리

arr = [ list(input()) for _ in range(N) ]
visit = [ [0] * M for _ in range(N) ]
ans = 0
visit[N-1][0] = 1
DFS(N-1,0)
print(ans)