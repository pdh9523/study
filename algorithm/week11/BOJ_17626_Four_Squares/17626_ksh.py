from math import sqrt

N = int(input())   # 1 ≤ n ≤ 50,000
sqrt1 = int(sqrt(N))

# 제곱수 1개
if N == sqrt1**2:
    exit(print(1))

# 제곱수 2개
for i in range(sqrt1, 0, -1):
    N2 = N - i**2
    if N2 == (int(sqrt(N2)))**2:
        exit(print(2))

# 제곱수 3개
for i in range(sqrt1, 0, -1):
    N2 = N - i**2
    sqrt2 = int(sqrt(N2))
    for j in range(sqrt2, 0, -1):
        N3 = N2 - j**2
        if N3 == (int(sqrt(N3)))**2:
            exit(print(3))

# 제곱수 4개
print(4)