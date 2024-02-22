# 수빈이가 이동하는 함수
def bfs(start, finish):      # 시작정점 start, 도착정점 finish
    q = []                   # 큐
    visited = [0] * 100001   # visited
    q.append(start)          # 시작점 인큐
    visited[start] = 1       # 시작점 방문 표시

    while q:              # 큐가 비워질 때까지 (남은 정점이 있으면)
        t = q.pop(0)      # t에서 갈 수 있는 정점 i
        # t 에서 할일
        cango = [t-1, t+1, 2*t]    # 갈 수 있는 3가지 지점
        for c in range(len(cango)):
            if cango[c] < 0 or cango[c] > 100000:
                cango[c] = start

        for i in cango:  # 갈 수 있는 3가지 지점을 순회
            if visited[i] == 0:    # 방문하지 않은 정점이면
                q.append(i)        # 인큐
                visited[i] = 1 + visited[t]   # 방문표시
            if i == finish:
                return visited[i] - 1

# 수빈이가 있는 위치 N, 동생이 있는 위치 K
N, K = map(int, input().split())

print(bfs(N, K))