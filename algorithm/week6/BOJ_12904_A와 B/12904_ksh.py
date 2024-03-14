S = list(input())
T = list(input())

for i in range(len(T) - len(S)):
    if T.pop() == 'B':
        T.reverse()

if T == S:
    print(1)
else:
    print(0)