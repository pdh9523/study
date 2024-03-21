# 어떻게 하냐?
# 회의실에서 가장 빨리 끝나는 회의를 찾는다.
# 끝난 시간 이후에 가장 빨리 끝나는 회의를 찾는다...
# 끝까지 ㄱㄱ
N = int(input()) # 회의의 수
time = [list(map(int, input().split())) for _ in range(N)] # 시작, 끝
time.sort(key=lambda x: (x[1],x[0])) # 빠른 시간으로도 찾아야함...

result = 0
com = [0, 0]
for t in time:
    if t[0] >= com[1]:
        result += 1
        com = t
print(result)