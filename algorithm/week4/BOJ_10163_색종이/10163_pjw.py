N = int(input())
arr = [[0]*1001 for _ in range(1001)]
col_pap = [list(map(int, input().split())) for _ in range(N)]  # 색종이에관한 입력
empty = []
for i in range(0, N):
    alpha = 0
    result = 0    
    for j in range(i+1, N):
        max1 = max(col_pap[i][0], col_pap[j][0])
        max2 = max(col_pap[i][1], col_pap[j][1])
        min1 = min(col_pap[i][0] + col_pap[i][2]-1, col_pap[j][0] + col_pap[j][2] -1)
        min2 = min(col_pap[i][1] + col_pap[i][3]-1, col_pap[j][1] + col_pap[j][3] -1)
        if min2-max2+1 > 0 and min1-max1 + 1 > 0:
            alpha = col_pap[i][2]*col_pap[i][3] - (min2 - max2 +1) * (min1 - max1 +1)
            result += alpha
    if result >= col_pap[0][2]*col_pap[0][3]:
        empty.append(result - col_pap[0][2]*col_pap[0][3])
    else:
        empty.append(result)

print(*empty)
print(col_pap[-1][2]*col_pap[-1][3])
