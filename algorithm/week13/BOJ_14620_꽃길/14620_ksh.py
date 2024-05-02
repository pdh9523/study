'22:54 - 23:48 | Python3 31120KB, 84ms | PyPy3 111548KB, 176ms'

N = int(input())                                               # 화단의 한 변의 길이 N
prices = [list(map(int, input().split())) for _ in range(N)]

flower_bed = [[0] * N for _ in range(N)]
for i in range(1, N-1):
    for j in range(1, N-1):
        flower_bed[i][j] = prices[i-1][j] + prices[i+1][j] + sum(prices[i][j-1:j+2])

result = float('inf')
for i in range(1, N-1):
    for j in range(1, N-1):
        for p in range(i, N-1):
            for q in range(1, N-1):
                done = [[i, j]]
                if p == i and q <= j:
                    continue
                if abs(i-p) + abs(j-q) >= 3:
                    for y in range(p, N - 1):
                        for x in range(1, N - 1):
                            if y == p and x <= q:
                                continue
                            done = [[i, j], [p, q]]
                            if abs(p-y) + abs(q-x) >= 3 and abs(i-y) + abs(j-x) >= 3:
                                s = 0
                                done = [[i, j], [p, q], [y, x]]
                                for a, b in done:
                                    s += flower_bed[a][b]
                                if result > s:
                                    result = s

print(result)



'''
[답 : 14]

6
1 1 1 1 1 1
1 1 1 1 1 1
1 1 3 1 1 1
1 1 1 1 1 1
1 1 1 1 1 5
1 0 1 1 1 1
'''