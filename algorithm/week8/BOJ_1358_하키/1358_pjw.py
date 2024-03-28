w, h, x, y, p = map(int, input().split()) # w,h 는 직사각형, x,y는 직사각형 왼쪽 아래 모서리 좌표, p는 선수
players = [list(map(int, input().split())) for _ in range(p)] # [i][0] = x, [i][1] = y

cnt = 0

for i in range(p):
    if abs(x - players[i][0])**2 + abs(y - players[i][1]+h/2)**2 <= (h/2)**2 and players[i][0] <= x:
        
        cnt += 1
    elif abs(x - players[i][0]+w)**2 + abs(y - players[i][1]+h/2)**2 <= (h/2)**2 and players[i][0] >= x+w:
        
        cnt += 1
    elif x <= players[i][0] <= x+w  and y <= players[i][1] <= y+h:
        
        cnt += 1
    else:
        continue

print(cnt)




