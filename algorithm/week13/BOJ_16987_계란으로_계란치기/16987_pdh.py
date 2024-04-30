def backtrack(idx=0):
    global ans
    # 순회 완료 시
    if idx == N:
        # 깨진 계란 개수 저장
        total = 0
        for i in range(N):
            if egg[i][0] <= 0:
                total += 1
        # 최대값 비교
        ans = max(ans,total)
        return
    
    # 현재 순회중인 계란이 깨져있으면
    if egg[idx][0] <= 0:
        # 다음 계란으로
        backtrack(idx+1)
        return

    # 전체 게란중에서
    for i in range(N):
        # 현재 계란 빼고
        if i == idx : continue
        # 깨져있지 않은 것을 체크
        if egg[i][0] > 0 :
            break
    # 다 깨져있으면
    else :
        # 현재 계란 빼고 다 깨져있으니 N-1
        ans = max(ans,N-1) 
        return

    # 백트래킹
    for i in range(N):
        if i == idx or egg[i][0] <= 0 : continue

        egg[idx][0] -= egg[i][1]
        egg[i][0] -= egg[idx][1]

        backtrack(idx+1)

        egg[idx][0] += egg[i][1]
        egg[i][0] += egg[idx][1]

# 입력
N = int(input())
egg = [ [*map(int,input().split())] for _ in range(N) ] #내구도와 무게

# 출력
ans = 0
backtrack()
print(ans)