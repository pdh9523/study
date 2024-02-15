N = int(input())
stack = []
for _ in range(N):
    arr = input().split()

    
    if arr[0]== 'push':
        stack.append(int(arr[1]))

    elif arr[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])

    elif arr[0] == 'size':
        print(len(stack))

    elif arr[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())

    elif arr[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
