# 피보나치
arr = [0,2,3]

N = int(input())
for i in range(3,N):
    arr.append((arr[i-1]+arr[i-2]))
print(arr[N-1])