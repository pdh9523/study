N = int(input())   # 색종이의 수
colors = [list(map(int, input().split())) for _ in range(N)]   # 색종이 위치 정보

paper = [[0] * 100 for _ in range(100)]   # 도화지
cnt = 0                                   # 색칠한 칸 수 세기
for color in colors:
    for i in range(10):
        for j in range(10):
            if paper[color[1] + i][color[0] + j] == 0:   # 비어있는 칸이면 칠하기
                paper[color[1] + i][color[0] + j] = 1
                cnt += 1

print(cnt)