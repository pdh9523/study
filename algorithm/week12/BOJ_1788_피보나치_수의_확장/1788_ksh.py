'21:56 ~ 22:14'

N = int(input())
if N == 0:
    x = 0
elif N == 1:
    x = 1
elif N > 0:
    a, b = 0, 1
    for i in range(N-1):
        a, b = b, a+b
    x = b
elif N < 0:
    N *= -1
    a, b = 0, 1
    for i in range(N-1):
        a, b = b, a-b
    x = b

if x == 0:
    print(0)
elif x > 0:
    print(1)
elif x < 0:
    print(-1)
print(abs(x) % 1000000000)



'메모리 초과'

'''
N = int(input())
if N == 0:
    x = 0
elif N == 1:
    x = 1
elif N > 0:
    pibo = [0] * (N+1)
    pibo[1] = 1
    for i in range(2, N+1):
        pibo[i] = pibo[i-1] + pibo[i-2]
    x = pibo[-1]
elif N < 0:
    N *= -1
    pibo = [0] * (N+1)
    pibo[1] = 1
    for i in range(2, N+1):
        pibo[i] = pibo[i-2] - pibo[i-1]
    x = pibo[-1]

if x == 0:
    print(0)
elif x > 0:
    print(1)
elif x < 0:
    print(-1)
print(abs(x) % 1000000000)
'''