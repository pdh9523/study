def travel(i, city, sum_cost):
    global min_total

    if i == N and city == start:   # N 번 이동을 완료하였고, 출발 지점으로 돌아왔다면
        if min_total > sum_cost:   # 이때까지의 비용 최솟값과 현재 비용을 비교하여
            min_total = sum_cost   # 비용 최솟값 업데이트하고 종료

    if sum_cost > min_total:   # 비용이 이때까지의 비용 최솟값보다 크다면
        return                 # 여행을 중단한다.

    for n in range(N):                                   # 도시들을 순회하며
        if visited[n] == 0 and cost[city][n] != 0:       # 방문하지 않았고, 갈 수 있는 도시를 찾아서
            visited[n] = 1                               # 방문 표시
            travel(i + 1, n, sum_cost + cost[city][n])   # 다음 도시로 여행
            visited[n] = 0                               # 방문 표시 초기화


N = int(input())   # 도시의 수
cost = [list(map(int, input().split())) for _ in range(N)]   # cost[i][j] : 도시 i에서 j로 가기 위한 비용
visited = [0] * N   # 방문한 도시들

min_total = 1000000 * N   # 여행 비용 최솟값 초기 설정
for start in range(N):    # 모든 도시를 순회하며 출발 지점으로 삼고
    travel(0, start, 0)   # 여행 떠나기

print(min_total)   # 최소 비용 출력