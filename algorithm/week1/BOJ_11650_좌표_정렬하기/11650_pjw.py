N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def sorting(xy):
    sorted_arr = sorted(xy, key=lambda x: (x[0], x[1]))
    for pair in sorted_arr:
        print(pair[0], pair[1])

sorting(arr)
