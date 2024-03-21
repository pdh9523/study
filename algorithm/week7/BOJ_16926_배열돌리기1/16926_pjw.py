# 크기가 4*5일때 x좌표가 0이나4, y좌표가 0이나 5일때 반시계방향으로 한칸씩돌림
# 다음은 0+1, 4-1, 0+1, 5-1 을 돌림
# 다음은 0+k, N-k, 0+k, M-k를 돌림... 언제까지? N-K or M-k가 N//2, M//2보다 작을때까지
# 왜틀리농...
def rotate_array(arr, N, M, R):
    k = 0
    while (N - 2*k) > 1 or (M - 2*k) > 1:
        # 회전할 테두리의 원소들을 저장할 리스트
        temp = []
        
        # 왼쪽 테두리 원소들을 저장
        for i in range(k, N - k):
            temp.append(arr[i][k])
        
        # 위쪽 테두리 원소들을 저장
        for j in range(k + 1, M - k):
            temp.append(arr[N - k - 1][j])
        
        # 오른쪽 테두리 원소들을 저장
        for i in range(N - k - 2, k - 1, -1):
            temp.append(arr[i][M - k - 1])
        
        # 아래쪽 테두리 원소들을 저장
        for j in range(M - k - 2, k, -1):
            temp.append(arr[k][j])
        
        # 회전
        if len(temp) != 0:
            rotate_temp = temp[-R % len(temp):] + temp[:-R % len(temp)]
        
            # 회전한 값을 다시 테두리에 넣어줍니다.
            idx = 0
            # 왼쪽 테두리
            for i in range(k, N - k):
                arr[i][k] = rotate_temp[idx]
                idx += 1
            
            # 위쪽 테두리
            for j in range(k + 1, M - k):
                arr[N - k - 1][j] = rotate_temp[idx]
                idx += 1
            
            # 오른쪽 테두리
            for i in range(N - k - 2, k - 1, -1):
                arr[i][M - k - 1] = rotate_temp[idx]
                idx += 1
            
            # 아래쪽 테두리
            for j in range(M - k - 2, k, -1):
                arr[k][j] = rotate_temp[idx]
                idx += 1
            
        # 다음 테두리로 이동
        k += 1

# 입력 받기
N, M, R = map(int, input().split()) # 배열 크기 및 회전 수
arr = [list(map(int, input().split())) for _ in range(N)] # 배열

rotate_array(arr, N, M, R)

for row in arr:
    print(*row)
