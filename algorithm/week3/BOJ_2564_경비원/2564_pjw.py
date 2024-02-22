N, M = map(int, input().split()) # N은 전체 블록의 가로 크기, M은 세로 크기
store_num = int(input()) # 가게 갯수
len_sum = 0 # 최단 거리 합 구할 거임
arr = [] # 빈 리스트 만들기
for j in range(store_num):
    direc, length = map(int, input().split()) # 동 1 서 2 남 3 북 4 
    # length는 1,2 일 경우 위쪽 경계와의 거리 / 3,4 일 경우 왼쪽 경계와의 거리
    arr.append([direc, length]) # 리스트에 각 상점의 방향과 거리 담기
    

dong_dir, dong_len = map(int, input().split()) # 동근이의 위치

for i in range(store_num):
    if dong_dir == 2:
        if arr[i][0] == 2:
            len_sum += abs(dong_len - arr[i][1])
        elif arr[i][0] == 4:
            len_sum += abs((N - dong_len) + (M - arr[i][1]))
        elif arr[i][0] == 3:
            len_sum += abs(dong_len + (M - arr[i][1]))
        else:
            dong1 = dong_len + M + arr[i][1]
            dong2 = N - dong_len + M + N - arr[i][1]
            len_sum += min(dong1, dong2)
    elif dong_dir == 1:
        if arr[i][0] == 1:
            len_sum += abs(dong_len - arr[i][1])
        elif arr[i][0] == 4:
            len_sum += abs((N - dong_len) + arr[i][1])
        elif arr[i][0] == 3:
            len_sum += abs(dong_len + arr[i][1])
        else:
            dong1 = dong_len + M + arr[i][1]
            dong2 = N - dong_len + M + N - arr[i][1]
            len_sum += min(dong1, dong2) # 검산 완료
    elif dong_dir == 4:
        if arr[i][0] == 4:
            len_sum += abs(dong_len - arr[i][1])
        elif arr[i][0] == 2:
            len_sum += abs((M - dong_len) + (N - arr[i][1]))
        elif arr[i][0] == 1:
            len_sum += abs(dong_len + (N - arr[i][1]))
        else:
            dong3 = dong_len + arr[i][1] + N
            dong4 = M - dong_len +  N + M - arr[i][1]
            len_sum += min(dong3, dong4)
    else:
        if arr[i][0] == 3:
            len_sum += abs(dong_len - arr[i][1])
        elif arr[i][0] == 2:
            len_sum += abs((M - dong_len) + arr[i][1])
        elif arr[i][0] == 1:
            len_sum += abs(dong_len + arr[i][1])
        else:
            dong3 = dong_len + arr[i][1] + N
            dong4 = M - dong_len +  N + M - arr[i][1]
            len_sum += min(dong3, dong4)

print(len_sum)