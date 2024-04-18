import sys
input = sys.stdin.readline
from collections import deque


for _ in range(int(input())):
    N, K = map(int, input().split())                               # 건물의 수 N, 건설순서 규칙의 수 K
    time = [0] + list(map(int, input().split()))                   # 각 건물당 공기
    orders = [list(map(int, input().split())) for _ in range(K)]   # 건설순서 정보
    W = int(input())                                               # 최종목표 건물 번호
    
    # 1. 건설순서 정보 가공
    pre = [[] for _ in range(N+1)]
    pre2 = [[] for _ in range(N+1)]
    for s, e in orders:
        pre[e].append(s)
        pre2[s].append(e)

    # 2. 진입차수 : 해당 작업을 하기 전에 선행되어야 하는 작업의 수
    indegree = []
    for i in range(N+1):
        indegree.append(len(pre[i]))

    # 3. dp
    dp = [0] * (N+1)

    # 3-1. 진입차수가 0인 건물 먼저 작업리스트(queue)에 담기
    queue = deque([])
    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = time[i]

    # 3-2. 작업리스트(queue)를 순회하며 진입차수 -= 1, 진입차수가 0인 건물 작업리스트(queue)에 담기
    while queue:
        x = queue.popleft()

        for y in pre2[x]:
            indegree[y] -= 1
            dp[y] = max(dp[y], time[y] + dp[x])

            if indegree[y] == 0:
                queue.append(y)

    print(dp[W])