import sys
input = sys.stdin.readline
 
N, K = map(int, input().split())
arr = list(input().strip())

ans = 0 
for i in range(N):
    #햄버거가 있으면
    if arr[i] == 'H':
        for j in range(i-K, i+K + 1):
            
            #주변에서 사람을 찾는다.
            if 0 <= j < N: 
                if arr[j] == 'P':
                    # 먹었으면 나가고
                    arr[j] = ''
                    ans += 1
                    break
print(ans)