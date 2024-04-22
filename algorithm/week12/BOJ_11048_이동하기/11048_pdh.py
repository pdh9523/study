N,M = map(int,input().split())

maze = [ [*map(int,input().split())] for _ in range(N) ]
# DP 리스트 초기화
DP = [ [0] * M for _ in range(N) ] 

for i in range(N) :
    for j in range(M) :
        if i > 0 and j > 0:                                                 # 일반적 경우(인덱스 범위 안벗어나는 경우)
            maze[i][j] += max(maze[i-1][j],maze[i][j-1],maze[i-1][j-1])     # i,j 좌표로 올 수 있는 최대값을 i,j 에 더해줌
        elif j == 0 and i > 0  :                                            # 세로줄은 쭉 더해줌
            maze[i][j] += maze[i-1][j]
        elif i == 0 and j > 0  :                                            # 가로줄도 쭉 더해줌
            maze[i][j] += maze[i][j-1]
# 결과 출력
print(maze[-1][-1]) 