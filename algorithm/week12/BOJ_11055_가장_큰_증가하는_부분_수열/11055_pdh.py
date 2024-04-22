N = int(input())

arr = list(map(int,input().split()))
# DP는 arr배열의 원래 값을 가지면서,
DP = arr[:]

# arr을 순회하면서 
for i in range(N-1):

    for j in range(i+1,N):
        # 뒤의 값이 더 크면 
        if arr[j] > arr[i] :
            # DP에 그 경우를 저장해둠
            DP[j] = max(DP[j], DP[i]+arr[j])
# 출력
print(max(DP))