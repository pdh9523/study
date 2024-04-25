n = int(input())

if n < 3:
    print(n)
else:
    a, b = 1, 2
    for _ in range(3, n + 1): # 피보나치
        a, b = b, (a + b) % 10

    print(b)
