N = int(input())
adjl = [list(map(lambda x: 1 if x == '1' else float('inf'), input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            adjl[i][j] = min(adjl[i][j], adjl[i][k] + adjl[k][j])

adjl = [list(map(lambda x: 1 if x != float('inf') else 0, adjl[i])) for i in range(N)]

for i in range(N):
    print(*adjl[i])