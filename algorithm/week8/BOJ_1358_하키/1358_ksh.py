import sys
input  = sys.stdin.readline

W, H, X, Y, P = map(int, input().split())   # 선수 P명 / H는 짝수
in_link = 0
for _ in range(P):
    x, y = map(int, input().split())

    if X <= x <= X+W and Y <= y <= Y+H:
        in_link += 1
    elif (x - X)**2 + (y - (Y+H//2))**2 <= (H//2)**2:
        in_link += 1
    elif (x - (X+W))**2 + (y - (Y+H//2))**2 <= (H//2)**2:
        in_link += 1

print(in_link)