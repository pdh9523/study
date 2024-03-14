def f(num, cnt):
    global min_cnt

    if num == 1:
        if min_cnt > cnt:
            min_cnt = cnt
    if cnt > min_cnt:
        return
    if num > 1:
        if num % 3 == 0:
            f(num // 3, cnt + 1)
        if num % 2 == 0:
            f(num // 2, cnt + 1)
        if num > 1:
            f(num - 1, cnt + 1)


N = int(input())

min_cnt = 1000000
f(N, 0)

print(min_cnt)