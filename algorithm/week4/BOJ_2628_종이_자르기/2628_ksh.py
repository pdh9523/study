X, Y = map(int, input().split())
N = int(input())
line = [list(map(int, input().split())) for _ in range(N)]

# 가로, 세로 경계선 좌표 담고 정렬
X_list = [0, X]
Y_list = [0, Y]
for l in line:
    if l[0] == 1:
        X_list.append(l[1])
    else:
        Y_list.append(l[1])
X_list.sort()
Y_list.sort()

# 가로, 세로 점선따라 잘랐을 때 가장 긴 변 구하기
X_max = 0
Y_max = 0
for i in range(len(X_list) - 1):
    if X_max < X_list[i + 1] - X_list[i]:
        X_max = X_list[i + 1] - X_list[i]
for j in range(len(Y_list) - 1):
    if Y_max < Y_list[j + 1] - Y_list[j]:
        Y_max = Y_list[j + 1] - Y_list[j]

# 결과 출력
print(X_max * Y_max)