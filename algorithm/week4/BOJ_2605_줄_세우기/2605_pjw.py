N = int(input())
arr = list(map(int, input().split()))

stu_line = []
stu_line.append(1)
alpha = 2

while alpha < N:
    for i in range(1, N):
        if arr[i] == 0:
            stu_line.append(alpha)
            alpha += 1
        else:
            stu_line.insert(i-arr[i],alpha)
            alpha += 1
print(*stu_line)