import sys

# 입력값 받기
N = int(input())
XYs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# bubble sort
while N != 0:
    for n in range(N - 1):
        # x 좌표 비교 후 정렬
        if XYs[n][0] > XYs[n + 1][0]:
            XYs[n], XYs[n + 1] = XYs[n + 1], XYs[n]
        elif XYs[n][0] == XYs[n + 1][0]:
            # x 좌표가 같을 때에는 y 좌표 비교 후 정렬
            if XYs[n][1] > XYs[n + 1][1]:
                XYs[n], XYs[n + 1] = XYs[n + 1], XYs[n]
    # while 문 대신 for (n과 다른 변수) in range(N - 1): 사용 가능
    N -= 1

# 언패킹으로 결과 출력
for XY in range(XYs):
    print(*XY)