W,H = map(int,input().split())      # 개미집

P,Q = map(int,input().split())      # 개미 위치

move = int(input())

W_move = move % (2*W)               # 개미집 2바퀴를 돌면 원위치로 옴 (X좌표 Y좌표 각각)
H_move = move % (2*H)   

w = 1                               # +/- 설정치
for _ in range(W_move):             # 2바퀴를 돈 나머지에 대해서
    P = P + (1 * w)                 # 개미 위치를 한칸씩 옮기다가
    if P == W or P == 0:            # 벽을 만나면
        w *= -1                     # 반대 방향으로 옮기기

w = 1
for _ in range(H_move):
    Q = Q + (1* w)
    if Q == H or Q == 0:
        w *= -1

print(P, Q)