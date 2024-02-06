# 보드판 정보 입력
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

# 경우마다 바꿔야 할 보드 수를 담을 빈 리스트 설정
# (단, 하나의 체스판 경우에 대해 2가지 경우 중 작은 수만 담는다.)
counts = []

# (0, 0) 을 기준으로 순회 범위 설정
# row 가 N 개, column 이 M 개
for n in range(N - 7):
    for m in range(M - 7):
        # 체스판에서 바꿔야 할 보드 수 변수 설정
        count = 0
        # 체스판 내에서 순회 (체스판 크기 : 8 * 8)
        for i in range(8):
            for j in range(8):
                # 좌표의 x 값과 y 값을 더한 값의 홀짝으로 격자 색깔 비교
                if (n + i + m + j) % 2 == 0:
                    if board[n + i][m + j] != 'W':
                        count += 1
                else:
                    if board[n + i][m + j] != 'B':
                        count += 1
        # 체스판의 좌측상단 첫 출발점이 W 인 경우를 기준으로
        # 바꿔야 할 보드 수를 구하고
        # 그 수가 체스판의 절반을 넘어가면
        # 첫 출발점이 B 인 경우가 바꿔야 할 보드 수가 더 적은 것이므로
        # 그 수를 counts 리스트에 append
        if count > 32:
            count = 64 - count
        counts.append(count)

# counts 리스트에서 최솟값을 구하여
# 결과 출력
print(min(counts))