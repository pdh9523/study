N = int(input()) # 보드
arr = [list(input()) for _ in range(N)] # 빨 C 파 P 초 Z 노 Y

def candy(arr):
    max_count = 0
    
    for i in range(N):
        count = 1
        for j in range(1, N):
            if arr[i][j] == arr[i][j-1]:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1 # 초기화 안하면 ㅈ댐
        max_count = max(max_count, count)
    
    for j in range(N):
        count = 1
        for i in range(1, N):
            if arr[i][j] == arr[i-1][j]:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
        max_count = max(max_count, count)
    
    return max_count

max_cnt = 0

for i in range(N):
    for j in range(N-1):
        if arr[i][j] != arr[i][j+1]:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            max_cnt = max(candy(arr), max_cnt)
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        
        if arr[j][i] != arr[j+1][i]:
            arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
            max_cnt = max(candy(arr), max_cnt)
            arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]

print(max_cnt)