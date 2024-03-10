N, K = map(int, input().split()) # N번 칸, 내구도 한계 K
A = list(map(int, input().split())) # 2N개 있을거임
robot = [0]*N
cnt = 0
while A.count(0) < K:
    cnt += 1
    A.insert(0, A.pop())
    robot.pop()
    robot.insert(0,0)
    for i in range(N):
        if robot[i] == 1:
            if i == N-1:
                robot[i] = 0 # 1단계
    for j in range(N-2, -1, -1):
        if robot[j] == 1 and A[j+1] >= 1 and robot[j+1] == 0:
            robot[j] = 0
            robot[j+1] = 1
            A[j+1] -= 1
            if j+1 == N-1:
                robot[j+1] = 0
        else:
            continue # 2단계
    
    if A[0] != 0:
        robot[0] = 1
        A[0] -= 1

print(cnt)
    
        
