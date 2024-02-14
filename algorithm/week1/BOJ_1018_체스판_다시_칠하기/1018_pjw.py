N, M = map(int, input().split())
arr = [list(map(str, input())) for _ in range(N)]

min_repaint = 100

for i in range(N - 7):
    for j in range(M - 7):
        repaint_count = 0

        for k in range(8):
            for l in range(8):
                # 출발위치 기준 칠할 색 확인
                if (i + k + j + l) % 2 == 0:
                    if arr[i + k][j + l] != 'W':
                        repaint_count += 1
                else:
                    if arr[i + k][j + l] != 'B':
                        repaint_count += 1

        # 다시 칠한 수가 최소인지 확인
        repaint_count = min(repaint_count, 64 - repaint_count)
        min_repaint = min(min_repaint, repaint_count)

print(min_repaint)