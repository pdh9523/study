N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]   # 좌측하단 꼭짓점 좌표 가로, 세로, 너비, 높이

easel = [[1000] * 1001 for _ in range(1002)]   # 빈 평면 설정

for n in range(N):   # 색종이 정보를 순회하며
    for j in range(paper[n][0], paper[n][0] + paper[n][2]):   # 세로
        for i in range(paper[n][1], paper[n][1] + paper[n][3]):   # 가로
            easel[i][j] = n

area = [0] * N   # 색종이 별 면적 정보를 담을 리스트 설정
for n in range(N):   # 색종이 정보를 순회하며
    for j in range(paper[n][1], paper[n][1] + paper[n][3]):   # 색종이 크기만큼만 순회
        area[n] += easel[j][paper[n][0] : paper[n][0] + paper[n][2]].count(n)
    print(area[n])

'''
시간 초과

for n in range(1, N + 1):
    for k in range(1002):
        area[n] += easel[k].count(n)
    print(area[n])
'''