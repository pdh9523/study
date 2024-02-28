w, h = map(int, input().split())   # 가로 w, 세로 h (좌측하단 (0, 0), 우측상단 (w, h))
p, q = map(int, input().split())   # 출발 지점 가로 p, 세로 q
t = int(input())

i = 1
j = 1

wt = t % (2 * w)
ht = t % (2 * h)

while wt > 0:
    wt -= 1
    p += j
    if p == 0 or p == w:   # 세로 경계에 부딪혔을 때
        j *= -1

while ht > 0:
    ht -= 1
    q += i
    if q == 0 or q == h:   # 세로 경계에 부딪혔을 때
        i *= -1

print(p, q)