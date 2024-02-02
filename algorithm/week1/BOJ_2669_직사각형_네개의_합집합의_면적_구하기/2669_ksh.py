# 사각형 좌측하단, 우측상단 좌표 입력
rectangulars = [list(map(int, input().split())) for _ in range(4)]

# 빈 스케치북 준비
sketchbook = [[0] * 100 for _ in range(100)]

# 4개의 각각의 사각형에 대하여 좌표 확인하고,
for n in range(4):
    x1 = rectangulars[n][0]
    y1 = rectangulars[n][1]
    x2 = rectangulars[n][2]
    y2 = rectangulars[n][3]

    # 스케치북에 칠하기
    for j in range(x1, x2):
        for i in range(y1, y2):
            sketchbook[i][j] += 1

# 칠해지지 않은 스케치북의 면적을 구해서
# 전체 면적과의 차로 칠해진 면적 구하기
not_area = 0
for i in range(100):
    not_area += sketchbook[i].count(0)
print(10000 - not_area)

# # 칠해진 면적 구하기
# area = 0
# for i in range(100):
#     for j in range(100):
#         if sketchbook[i][j] >= 1:
#             area += 1
# print(area)