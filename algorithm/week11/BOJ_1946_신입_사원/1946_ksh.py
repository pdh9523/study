import sys
input = sys.stdin.readline

for t in range(int(input())):
    N = int(input())   # 지원자의 숫자 N
    cdds = [list(map(int, input().split())) for _ in range(N)]   # 서류심사 성적, 면접 성적의 순위

    cdds.sort()
    cnt, std = 1, cdds[0][1]

    for i in range(1, N):
        if cdds[i][1] < std:
            std = cdds[i][1]
            cnt += 1

    print(cnt)