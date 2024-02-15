N = int(input())

for _ in range(N):
    arr = input()
    stack = []
    is_valid = True

    for i in arr:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                is_valid = False
                break

    if stack:
        is_valid = False

    if is_valid:
        print('YES')
    else:
        print('NO')
