'복습하기'

import sys
input = sys.stdin.readline

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]   # [x, y]

area = 0
for i in range(N):
    j = (i + 1) % N  # 다음 점, 마지막 점에서는 다시 첫 번째 점으로
    area += points[i][0] * points[j][1] - points[j][0] * points[i][1]

area = abs(area) / 2
print(f'{area:.01f}')