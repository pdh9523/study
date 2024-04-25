N, K = map(int, input().split())

if K < 0:
    print(0)
elif K > N:
    print(0)
else:
    x = N
    resultN = 1
    while x > 0:
        resultN *= x
        x -= 1
    y = K
    resultK = 1
    while y > 0:
        resultK *= y
        y -= 1
    z = N - K
    resultZ = 1
    while z > 0:
        resultZ *= z
        z -= 1
    print((resultN // (resultK*resultZ)) % 10007)
    
'''
오답 코드
print(int((resultN / (resultK*resultZ)) % 10007))
'''