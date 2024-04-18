from collections import deque

def craft(N, K, D, arr, W):
        graph = [[] for _ in range(N+1)]
        indegree = [0] * (N+1)
        time = [0] * (N+1)

        for from_, to_ in arr:
            graph[from_].append(to_)
            indegree[to_] += 1

        
        queue = deque()
        for i in range(1, N+1):
            if indegree[i] == 0:
                queue.append(i)
                time[i] = D[i-1]
        
        while queue:
            current = queue.popleft()

            for next in graph[current]:
                indegree[next] -= 1
                time[next] = max(time[next], time[current] + D[next-1])
                if indegree[next] == 0:
                    queue.append(next)

        return time[W]

T = int(input()) # 테케

for tc in range(T):
    N, K = map(int, input().split()) # 건물 수 , 건설 순서 규칙
    D = list(map(int, input().split())) # 건물 당 건설 시간
    arr = [tuple(map(int, input().split())) for _ in range(K)] # 연결
    W = int(input()) # 타깃

    # 위상정렬 - 창호햄 시작친구와 연결된 거에서 max값을 누적시켜서, target까지 가면된다.

    print(craft(N, K, D, arr, W))