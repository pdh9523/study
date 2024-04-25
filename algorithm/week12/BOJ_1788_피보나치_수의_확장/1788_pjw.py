n = int(input()) # 1~ 백만 (절댓값)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(abs(n) - 1):
        a, b = b, a + b
    return a if n > 0 else -a

result = fibonacci(n)

if result > 0:
    print(1)
elif result == 0:
    print(0)
else:
    print(-1)
print(abs(result) % 1000000000)
