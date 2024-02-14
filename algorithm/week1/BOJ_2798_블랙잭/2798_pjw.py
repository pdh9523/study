N, M = map(int, input().split())
arr = list(map(int, input().split()))
max1 = 0
result = 0
for i in range(N):
    if arr[i] <= M: # M보다 큰 수를 입력받으면 거르기
        for j in range(i + 1, N): # i 다음꺼부터 보면됨
            if arr[i] + arr[j] <= M: # 만약 i와 이후의 수를 더한 것 중에 M보다 작은것이 있다면
                for k in range(j + 1, N): # j 다음꺼부터 보면된다
                    if arr[i] + arr[j] + arr[k] <= M: # 이거 3개 더한게 M보다 작으면
                        result = arr[i] + arr[j] + arr[k]
                        if max1 < result: # M보다 작은 수 중 가장 큰 수를 찾는다.
                            max1 = result
print(max1)