N = int(input())  # 삼각형의 크기(줄 수)
arr = [list(map(int, input().split())) for _ in range(N)]  # 정수 삼각형 입력


max_sum = [[0] * N for _ in range(N)]
max_sum[0][0] = arr[0][0]  # 이거 하나밖에 없어서 최대

# 첫 번째는 걍 1개라 위에 박아놈
for i in range(1, N):
    for j in range(i + 1):
        if j == 0:  # 각 행의 첫 번째 열은 바로 위 행의 첫 번째 열만 가능
            max_sum[i][j] = max_sum[i - 1][j] + arr[i][j]
        elif j == i:  # 각 행의 마지막 열은 바로 위 행의 마지막 열만 가능
            max_sum[i][j] = max_sum[i - 1][j - 1] + arr[i][j]
        else:  # 나머지 경우에는 위 행의 두 개 열 중 큰 값을 선택하여 더함
            max_sum[i][j] = max(max_sum[i - 1][j - 1], max_sum[i - 1][j]) + arr[i][j]

# 최대 합 중 가장 큰 값을 찾음
max_triangle_sum = max(max_sum[N - 1])

print(max_triangle_sum)


