N = int(input()) # 색종이 수
arr = [list(map(int, input().split())) for _ in range(N)]
big_picture = [[0] * 100 for _ in range(100)]

for i in range(N):
    a1 = arr[i][0]
    a2 = arr[i][1]
    for j in range(a1, a1 + 10):
        for k in range(a2, a2 + 10):
            if big_picture[j][k] == 0:
                big_picture[j][k] = 1

alpha = 0
for row in big_picture:
    alpha += row.count(1)
print(alpha)