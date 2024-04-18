n = int(input())  # 주어진 수 개수
target = []
for _ in range(n):
    target.append(int(input()))

stack = []
result = []
chul = []
current = 1

for num in target:
    while current <= num:
        stack.append(current)
        chul.append('+')
        current += 1
    if stack[-1] == num:
        stack.pop()
        chul.append('-')
    else:
        print('NO')
        exit(0)

for operation in chul:
    print(operation)
