import sys
input = sys.stdin.readline

N = int(input())
num = [int(input()) for _ in range(N)]

stack, result = [], []
idx = 0

for i in range(1, N+1):
    stack.append(i)
    result.append('+')
    while stack and stack[-1] == num[idx]:
        stack.pop()
        result.append('-')
        idx += 1

if result.count('+') == result.count('-'):
    for i in range(len(result)):
        print(result[i])
else:
    print('NO')