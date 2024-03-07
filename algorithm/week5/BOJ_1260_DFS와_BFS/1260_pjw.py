from collections import deque

# DFS 함수 정의
def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for next in graph[start]:
        if not visited[next]:
            dfs(graph, next, visited)

# BFS 함수 정의
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for next in graph[v]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True


N, M, V = map(int, input().split()) # 정점 갯수, 간선 갯수, 정점 번호

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split()) # 양방향
    graph[a].append(b)
    graph[b].append(a)

# 경로가 여러개면 작은 걸로가기
for i in graph:
    i.sort()

#초기화
visited = [False] * (N + 1)

# DFS
dfs(graph, V, visited)
print()

#초기화
visited = [False] * (N + 1)

# BFS
bfs(graph, V, visited)