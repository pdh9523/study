def counting(candies):
    global maximum

    for a in range(N):
        temp1, temp2 = 1, 1
        for b in range(1, N):
            if candies[a][b] == candies[a][b-1]:
                temp1 += 1
            else:
                if temp1 > maximum:
                    maximum = temp1
                temp1 = 1
            if candies[b][a] == candies[b-1][a]:
                temp2 += 1
            else:
                if temp2 > maximum:
                    maximum = temp2
                temp2 = 1

        if temp1 > maximum:
            maximum = temp1
        if temp2 > maximum:
            maximum = temp2
        if maximum == N:
            exit(print(N))


N = int(input())
candies = [list(input()) for _ in range(N)]   # 빨간색 C, 파란색 P, 초록색 Z, 노란색 Y

maximum = 0

di = [[1, 0], [0, 1]]
for i in range(N):
    for j in range(N):
        for k in range(2):
            p, q = i + di[k][0], j + di[k][1]
            if 0 <= p < N and 0 <= q < N:
                if candies[i][j] != candies[p][q]:
                    candies[i][j], candies[p][q] = candies[p][q], candies[i][j]
                    counting(candies)
                    candies[i][j], candies[p][q] = candies[p][q], candies[i][j]

print(maximum)