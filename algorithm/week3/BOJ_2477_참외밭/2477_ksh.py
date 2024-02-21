K = int(input())   # 단위면적당 참외의 개수 (1 <= K <= 20)
field = [list(map(int, input().split())) for _ in range(6)]

length = []   # 길이
width = []    # 동, 서 길이
height = []   # 남, 북 길이
for i in range(6):
    length.append(field[i][1])
    if field[i][0] in [1, 2]:   # 동서 길이이면
        width.append(field[i][1])
    else:                       # 남북 길이이면
        height.append(field[i][1])

large = max(width) * max(height)   # 동서, 남북 길이 중 가장 긴 길이의 곱
wi = length.index(max(width))      # width_max_index
he = length.index(max(height))     # height_max_index
small = length[wi - 3] * length[he - 3]   # 가장 긴 변의 길이 3개 전후로 제해야 하는 작은 사각형의 변의 길이가 있다.

melon = K * (large - small)   # 단위 면적 당 참외 수 * (큰 사각형 - 작은 사각형)
print(melon)