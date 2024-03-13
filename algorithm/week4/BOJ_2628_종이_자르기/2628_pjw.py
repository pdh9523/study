width, height = map(int, input().split())
N = int(input())
cut_work = [list(map(int, input().split())) for _ in range(N)]
# 가로는 cut_work[i][0] = 0, 세로는 cut_work[i][0] = 1

max1 = 0
max2 = 0

cut_height = []
cut_width = []
for i in range(N):
    if cut_work[i][0] == 1:
        cut_height.append(cut_work[i][1])
    else:
        cut_width.append(cut_work[i][1])

cut_height.insert(0, 0) # 걍 만들때 0 넣고 시작해도 될듯
cut_height.append(width)
cut_width.insert(0, 0)
cut_width.append(height)

cut_width.sort()
cut_height.sort()

for j in range(len(cut_width)-1):
    if max1 < cut_width[j+1] - cut_width[j]:
        max1 = cut_width[j+1] - cut_width[j]

for k in range(len(cut_height)-1):
    if max2 < cut_height[k+1] - cut_height[k]:
        max2 = cut_height[k+1] - cut_height[k]


area = max1 * max2

print(area)