import sys

board = [[0] * 1001 for _ in range(1001)]

t = int(input())

for k in range(1,t+1):
    i,j, i_length, j_length = map(int,sys.stdin.readline().strip().split())
    
    for idx in range(i,i+i_length):                 # 사각형 칠하기
        for jdx in range(j,j+j_length):             
            board[idx][jdx] = k                     # 덧칠하면서 가려지는 부분은 사라짐 (순서대로 k가 1,2,3,4씩 증가하므로 구분 가능)

for a in range(1,t+1):
    output = 0 
    for b in range(1001):
        output += board[b].count(a)                 # 다 칠한 후 1,2,3,4 씩 개수를 세어 출력
    print(output)