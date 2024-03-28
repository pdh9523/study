arr = [list(map(int, input().split())) for _ in range(3)] # 1, 2, 3

alpha = ((arr[1][0]-arr[0][0])*(arr[2][1]-arr[0][1])-(arr[1][1]-arr[0][1])*(arr[2][0]-arr[0][0]))
if alpha > 0:
    print(1)
elif alpha < 0:
    print(-1)
else:
    print(0)