N = int(input())
alpha = []
sum_all = 0

def factorial(n):
    if n == 0 or n ==  1:
        return 1
    else:
        return n * factorial(n-1)

for i in range(10):
    sum_all += factorial(i)
    if sum_all > N:
        break
    alpha.append(sum_all)

if N not in alpha:
    print('NO')
else:
    print('YES')