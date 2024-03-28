def count_visible(buildings, i):
   
    visible = 0
    left_max = float('-inf')
    right_max = float('-inf')
    for j in range(i - 1, -1, -1):  # 왼쪽에 있는 건물들 검사
        if (buildings[j] - buildings[i]) / abs(j - i) > left_max:
            left_max = (buildings[j] - buildings[i]) / abs(j - i)
            visible += 1
    for k in range(i + 1, len(buildings)):  # 오른쪽에 있는 건물들 검사
        if (buildings[k] - buildings[i]) / abs(k - i) > right_max:
            right_max = (buildings[k] - buildings[i]) / abs(k - i)
            visible += 1
    return visible

def most_visible(buildings):
   
    max_visible = 0
    for i in range(len(buildings)):
        visible = count_visible(buildings, i)
        max_visible = max(max_visible, visible)
    return max_visible


n = int(input())
building_heights = list(map(int, input().split()))
result = most_visible(building_heights)
print(result)