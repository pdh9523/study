N = int(input())
sec_num = []
max1 = 0
for i in range(N, N//2-1, -1):
    sec_num.append(i)

for num in sec_num:
    empty = []
    empty.append(N)
    empty.append(num)

    while empty[-2] - empty[-1] >= 0:
        alpha = empty[-2] - empty[-1]
        empty.append(alpha)

    if max1 < len(empty):
        max1 = len(empty)
        real_empty = empty
print(max1)
print(*real_empty)