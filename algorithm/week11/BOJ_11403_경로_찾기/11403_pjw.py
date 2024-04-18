from collections import deque

def bfs(graph, start):
    n = len(graph)
    visited = [False] * n
    queue = deque()

    queue.append(start)

    while queue:
        node = queue.popleft()
        for i in range(n):
            if graph[node][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)

    return visited

def find_paths(graph):

    paths = []

    for i in range(n):
        paths.append(bfs(graph, i))

    return paths

n = int(input()) # n개의 점
graph = [list(map(int, input().split())) for _ in range(n)] # 정보

paths = find_paths(graph)
for path in paths:
    print(' '.join(map(lambda x: '1' if x else '0', path)))
