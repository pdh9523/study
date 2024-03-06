def dfs(x, val, depth=1):
    global cost # 비용 계산
    global first
    global n # 도시 수

    if depth == n: # 계산 종료
        for nx, _cost in graph[x]:
            if nx == first:
                cost = min(cost, val+_cost) # 가장 적은 코스트 반환
        return

    if visit[x]:
        return

    visit[x] = 1

    for nx, _cost in graph[x]:
        if not visit[nx]: # 방문 안했다면
            dfs(nx, val+_cost, depth+1) # 한개씩 올려주고
            visit[nx] = 0 # 방문 초기화


n = int(input())
graph = [[] for _ in range(n)] # 빈 그래프 하나 만들자
cost = float('inf') # 최소 구해야 하므로 걍 inf로 지정

for i in range(n):
    arr = list(map(int, input().split())) # 한 줄 씩 받을 거임
    for j in range(n):
        if i == j or arr[j] == 0: # 같은 도시와 0인 도시는 이동 불가
            continue
        graph[i].append((j, arr[j])) # 그래프에 넣을거야

for i in range(n): # 어느 도시에서든 출발할 수 있음
    visit = [0] * n # 방문 기록을 남겨야함
    first = i
    dfs(i, 0)

print(cost)