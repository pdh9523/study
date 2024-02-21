N = int(input())
columns = []

# 입력받은 기둥 정보를 리스트에 저장
for _ in range(N):
    L, H = map(int, input().split())
    columns.append((L, H))

# 가장 높은 기둥의 위치 찾기
max_height = max(column[1] for column in columns)
max_height_index =  columns[max_height][0]

# 왼쪽에서 가장 높은 기둥까지의 면적 계산
area_left = 0
current_height = 0
for i in range(max_height_index):
    current_height = max(current_height, columns[i][1])
    area_left += current_height

# 오른쪽에서 가장 높은 기둥까지의 면적 계산
area_right = 0
current_height = 0
for i in range(N - 1, max_height_index, -1):
    current_height = max(current_height, columns[i][1])
    area_right += current_height

# 최종 면적 계산
total_area = (max_height_index + 1) * max_height  # 가장 높은 기둥의 면적

# 왼쪽과 오른쪽 영역의 면적을 합산
total_area += area_left + area_right

# 결과 출력
print(total_area)









