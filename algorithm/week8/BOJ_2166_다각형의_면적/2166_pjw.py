N = int(input()) # N개의 점으로 이루어진 다각형
arr = [list(map(int, input().split())) for _ in range(N)] # arr[i][0] = x, arr[i][1] = y

# 가우스의 면적 공식 사용을 위해 할당할 result
result1 = 0
result2 = 0

for i in range(N-1):
    result1 += arr[i][0] * arr[i+1][1]
result1 += arr[N-1][0] * arr[0][1]

for j in range(N-1):
    result2 += arr[j][1] * arr[j+1][0]
result2 += arr[N-1][1] * arr[0][0]

# 가우스 면적공식 => 어느 다각형의 면적 A는 1/2 * abs((x1y2+x2y3+...xny1)-(y2x1+y3x2+...ynx1))
A = 0.5 * abs(result1 - result2)
print(A)