N, M = map(int, input().split())
S = input().strip()
T = input().strip()

S_index = []
for i in range(len(S)):
    if S[i] =='1':
        S_index.append(i)

T_index = []
for j in range(len(T)):
    if T[j] == '1':
        T_index.append(j)

result = []
for i in range(M):
    result.append(abs(S_index[i] - T_index[i]))

alpha = sum(result)
if alpha % 2 == 0:
    x = alpha//2
    print(2*(x**2))
else:
    x = alpha//2
    y = alpha - x
    print(x**2+y**2)