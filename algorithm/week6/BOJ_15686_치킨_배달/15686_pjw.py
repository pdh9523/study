from itertools import combinations

N, M = map(int, input().split())  # 도시의 크기, 치킨집
chicken = [list(map(int, input().split())) for _ in range(N)]  # 치킨

chicken_loc = []
house_loc = []
for i in range(N):
    for j in range(N):
        if chicken[i][j] == 2:
            chicken_loc.append([i, j])
        elif chicken[i][j] == 1:
            house_loc.append([i, j])
# 이거 따로 안넣어도 되네;;
# if len(chicken_loc) == M: # 폐업 안해도됨
#     distance = []
#     for i in range(len(chicken_loc)):
#         result = 0
#         empty = []
#         for j in range(len(house_loc)):
#             result = abs(chicken_loc[i][0] - house_loc[j][0]) + abs(chicken_loc[i][1] - house_loc[j][1])
#             empty.append(result)
#         distance.append(min(empty))

#     print(sum(distance))

min_distance = 3000
for selected_chickens in combinations(chicken_loc, M):
    total_distance = 0
    for house in house_loc:
        min_house_distance = 101
        for chicken_loc in selected_chickens:
            distance = abs(chicken_loc[0] - house[0]) + abs(chicken_loc[1] - house[1])
            min_house_distance = min(min_house_distance, distance)
        total_distance += min_house_distance
    min_distance = min(min_distance, total_distance)
print(min_distance)

    