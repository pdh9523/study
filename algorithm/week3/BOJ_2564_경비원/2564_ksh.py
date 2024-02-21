width, height = map(int, input().split())
N = int(input())   # 상점의 수
# [방향 : 1234 - 북남서동, 경계로부터의 거리]
location = [list(map(int, input().split())) for _ in range(N)]
dong = list(map(int, input().split()))

sums = 0
for i in range(N):
    if location[i][0] == dong[0]:   # 동근이와 상점이 같은 라인에 있을 때
        di = abs(location[i][1] - dong[1])
    elif [dong[0], location[i][0]] in [[1, 2], [2, 1]]:   # 동근, 상점 : 남, 북
        di = dong[1] + height + location[i][1]
        if di > width + height:
            di = 2 * (width + height) - di
    elif [dong[0], location[i][0]] in [[3, 4], [4, 3]]:   # 동근, 상점 : 동, 서
        di = dong[1] + width + location[i][1]
        if di > width + height:
            di = 2 * (width + height) - di
    elif [dong[0], location[i][0]] in [[1, 3], [3, 1]]:   # 동근, 상점 : 북, 서
        di = dong[1] + location[i][1]
    elif [dong[0], location[i][0]] in [[2, 4], [4, 2]]:   # 동근, 상점 : 남, 동
        di = width + height - dong[1] - location[i][1]
    elif dong[0] == 2 and location[i][0] == 3:            # 동근 : 남, 상점 : 서
        di = dong[1] + height - location[i][1]
    elif dong[0] == 3 and location[i][0] == 2:            # 동근 : 서, 상점 : 남
        di = location[i][1] + width - dong[1]
    elif dong[0] == 1 and location[i][0] == 4:            # 동근 : 북, 상점 : 동
        di = location[i][1] + width - dong[1]
    elif dong[0] == 4 and location[i][0] == 1:            # 동근 : 동, 상점 : 북
        di = dong[1] + width - location[i][1]
    sums += di

print(sums)