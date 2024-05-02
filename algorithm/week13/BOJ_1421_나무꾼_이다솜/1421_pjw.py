N, C, W = map(int, input().split())  # 나무 수, 비용, 나무 가격
arr = [int(input()) for _ in range(N)]  # 나무 길이

betta = []
for length in range(1, max(arr)+1):
    alpha = 0
    gamma = 0
    for i in range(N):
        if arr[i] > 1:
            alpha += arr[i] // length
            # print(f'alpha : {alpha}')
        elif arr[i] == 1 and length == 1:
            gamma += arr[i]

            # print(f'gamma : {gamma}')
    if 1 in arr:
        betta.append((alpha+gamma)*length*W - (alpha-1)*C)
    else:
        betta.append((alpha+gamma)*length*W - alpha*C)

print(max(betta))