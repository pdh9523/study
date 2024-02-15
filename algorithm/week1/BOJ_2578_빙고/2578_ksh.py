board = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]

cnt = 0
bingo = 0

for n in range(5):
    for c in call[n]:
        cnt += 1

        # 사회자가 부르는 수 지우기
        for i in range(5):
            if c in board[i]:
                board[i][board[i].index(c)] = 0
                break

        # 빙고 검증
        if cnt >= 10:
            bingo = 0
            cross1 = []
            cross2 = []
            for j in range(5):
                # 행
                if board[j] == [0, 0, 0, 0, 0]:
                    bingo += 1
                # 열
                if board[0][j] == board[1][j] == board[2][j] == board[3][j] == board[4][j] == 0:
                    bingo += 1
                cross1.append(board[j][j])
                cross2.append((board[j][4 - j]))
            # 대각선
            if cross1 == [0] * 5:
                bingo += 1
            if cross2 == [0] * 5:
                bingo += 1

        if bingo >= 3:
            print(cnt)
            break

    if bingo >= 3:
        break