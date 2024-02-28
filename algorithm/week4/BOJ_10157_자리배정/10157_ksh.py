C, R = map(int, input().split())   # 가로 C, 세로 R / (x, y)
K = int(input())

if C * R < K:   # 주어진 번호가 좌석 수보다 클 때
    print(0)
else:           # 주어진 번호가 좌석 수 이하일 때
    hall = [[0] * C for _ in range(R)]
    dx = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    k = 0
    i, j = 0, 0
    while True:
        K -= 1
        hall[i][j] = 1
        if K == 0:
            break
        i += dx[k % 4][0]
        j += dx[k % 4][1]

        if 0 <= i < R and 0 <= j < C:
            if hall[i][j] != 0:
                i -= dx[k % 4][0]
                j -= dx[k % 4][1]
                k += 1
                i += dx[k % 4][0]
                j += dx[k % 4][1]
        else:
            i -= dx[k % 4][0]
            j -= dx[k % 4][1]
            k += 1
            i += dx[k % 4][0]
            j += dx[k % 4][1]

    print(j + 1, i + 1)