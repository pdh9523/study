from math import ceil

N, K = map(int, input().split()) # N: 참가 학생수 K: 한 방 최대인원
arr = [list(map(int, input().split())) for _ in range(N)] # S = 0 : 여 S = 1 : 남 Y = 학년

grade_1_g = []
grade_1_b = []
grade_2_g = []
grade_2_b = []
grade_3_g = []
grade_3_b = []
grade_4_g = []
grade_4_b = []
grade_5_g = []
grade_5_b = []
grade_6_g = []
grade_6_b = []

for i in range(N):
    if arr[i][1] == 1:
        if arr[i][0] == 0:
            grade_1_g.append(arr[i][0])
        else:
            grade_1_b.append(arr[i][0])
    elif arr[i][1] == 2:
        if arr[i][0] == 0:
            grade_2_g.append(arr[i][0])
        else:
            grade_2_b.append(arr[i][0])
    elif arr[i][1] == 3:
        if arr[i][0] == 0:
            grade_3_g.append(arr[i][0])
        else:
            grade_3_b.append(arr[i][0])
    elif arr[i][1] == 4:
        if arr[i][0] == 0:
            grade_4_g.append(arr[i][0])
        else:
            grade_4_b.append(arr[i][0])
    elif arr[i][1] == 5:
        if arr[i][0] == 0:
            grade_5_g.append(arr[i][0])
        else:
            grade_5_b.append(arr[i][0])
    else:
        if arr[i][0] == 0:
            grade_6_g.append(arr[i][0])
        else:
            grade_6_b.append(arr[i][0])
g1b = ceil(len(grade_1_b)/K)
g1g = ceil(len(grade_1_g)/K)
g2b = ceil(len(grade_2_b)/K)
g2g = ceil(len(grade_2_g)/K)
g3b = ceil(len(grade_3_b)/K)
g3g = ceil(len(grade_3_g)/K)
g4b = ceil(len(grade_4_b)/K)
g4g = ceil(len(grade_4_g)/K)
g5b = ceil(len(grade_5_b)/K)
g5g = ceil(len(grade_5_g)/K)
g6b = ceil(len(grade_6_b)/K)
g6g = ceil(len(grade_6_g)/K)

result = g1b + g1g + g2b + g2g + g3b + g3g + g4b + g4g + g5b + g5g +g6b +g6g
print(result)