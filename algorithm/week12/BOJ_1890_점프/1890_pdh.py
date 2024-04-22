N = int(input())

arr = [ [*map(int,input().split())] for _ in range(N) ]
# DP 리스트를 설정 
DP = [ [0] * N for _ in range(N) ]

DP[0][0] = 1
for i in range(N):
    for j in range(N):
        tmp = arr[i][j]                 # arr[i][j]의 값을 설정하고
        
        if tmp == 0 :                   # 0 인 경우(사실 마지막) > 아무일도 하지 않기
            continue
        if 0 <= i + tmp < N :           # i+tmp가 인덱스 이내인 경우 그 위치에 값 합산
            DP[i+tmp][j] += DP[i][j]
        if 0 <= j + tmp < N :           # j+tmp가 인덱스 이내인 경우 그 위치에 값 합산
            DP[i][j+tmp] += DP[i][j]
print(DP[-1][-1])                       # 결과 출력