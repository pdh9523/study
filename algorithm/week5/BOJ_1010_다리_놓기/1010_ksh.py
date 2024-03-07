for _ in range(int(input())):
    W, E = map(int, input().split())

    result = 1
    for _ in range(W):
        result *= (E / W)
        E -= 1
        W -= 1

    print(round(result))