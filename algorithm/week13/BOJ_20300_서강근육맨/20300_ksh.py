'20:51 - 20:58'

N = int(input())
data = list(map(int, input().split()))

data.sort()
if N % 2 == 1:
    data.pop()
    N -= 1

result = 0
for i in range(N//2):
    if data[i] + data[N-i-1] > result:
        result = data[i] + data[N-i-1]

print(result)