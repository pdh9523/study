import sys
sys.setrecursionlimit(100000000)

from copy import deepcopy

def dicer(n, m):
    global cnt
    global dice2
    up = dice2[n][m - 3]
    if m > 2:
        dice2[n].pop(m)
        dice2[n].pop(m - 3)
    else:
        dice2[n].pop(m - 3)
        dice2[n].pop(m)
    cnt += max(dice2[n])
    if n == N - 1:
        return cnt
    else:
        n += 1                   # 다음 주사위로 index 보정
        m = dice2[n].index(up)   # 현재 주사위가 다음 주사위의 아랫면이 됨
        return dicer(n, m)       # 재귀 함수



N = int(input())   # 주사위의 개수
dice = [list(map(int, input().split())) for _ in range(N)]

dice2 = [[] for _ in range(N)]
for i in range(N):   # index -3 자리에 반대편 자리가 되도록 정리
    dice2[i] = dice[i][:3]
    dice2[i].append(dice[i][5])
    dice2[i].append(dice[i][3])
    dice2[i].append(dice[i][4])

dice3 = deepcopy(dice2)

cnts = []
for m in range(6):     # 주사위 칸마다 순회하면서
    cnt = 0
    cnts.append(dicer(0, m))
    dice2 = deepcopy(dice3)   # 주사위 정보 리셋

print(max(cnts))