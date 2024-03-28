N = int(input())                           # N : 빌딩의 수
height = list(map(int, input().split()))   # 빌딩의 높이

# 기울기 : 왼쪽 옥상 좌표, 오른쪽 옥상 좌표
# 기울기 연속적으로 증가하는 수 확인하기
# 본인 기준으로 좌측은 본인 - 비교하는 건물 / 왼쪽으로 점점 멀어지니까 기울기 연속적으로 감소 여부 확인
# 본인 기준으로 우측은 비교하는 건물 - 본인 / 오른쪽으로 점점 멀어지니까 기울기 연속적으로 증가 여부 확인
# 본인 : (i, height[i])

best_view = 0
for i in range(N):
    left = []
    right = []
    for l in range(i-1, -1, -1):                          # 좌측 빌딩 확인
        inclination = (height[i] - height[l]) / (i - l)
        left.append(inclination)
    for r in range(i+1, N):                               # 우측 빌딩 확인
        inclination = (height[r] - height[i]) / (r - i)
        right.append(inclination)

    view = 0
    if left:
        view += 1
        if len(left) > 1:
            for p in range(1, len(left)):
                if left[p] < left[p - 1]:
                    view += 1
                else:
                    left[p] = left[p - 1]
    if right:
        view += 1
        if len(right) > 1:
            for p in range(1, len(right)):
                if right[p] > right[p - 1]:
                    view += 1
                else:
                    right[p] = right[p - 1]

    if view > best_view:
        best_view = view

print(best_view)

