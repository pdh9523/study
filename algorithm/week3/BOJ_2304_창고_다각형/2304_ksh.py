N = int(input())   # N : 기둥의 개수
column = [list(map(int, input().split())) for _ in range(N)]   # L : 기둥의 시작 위치(왼쪽 면의 위치), H : 높이

column.sort(key=lambda c: c[0])   # 기둥 순서대로 정렬
height = column[:]
height.sort(key=lambda c: c[1], reverse=True)   # 높이 순서대로 정렬

warehouse = height[0][1]   # 창고 면적 변수 설정

# 좌측 끝부터 height[0][0] 까지
keep_going = True
high = height[0]
while keep_going == True:
    waitlist = column[ : column.index(high)]
    sec_high = [0, 0]
    for w in waitlist:
        if w[1] > sec_high[1]:
            sec_high = w
    warehouse += (high[0] - sec_high[0]) * sec_high[1]
    high = sec_high
    if high == column[0] or high == [0, 0]:
        keep_going = False

# height[0][0] 부터 우측 끝까지
keep_going = True
high = height[0]
while keep_going == True:
    waitlist = column[column.index(high) + 1 : ]
    sec_high = [0, 0]
    for w in waitlist:
        if w[1] > sec_high[1]:
            sec_high = w
    warehouse += (sec_high[0] - high[0]) * sec_high[1]
    high = sec_high
    if high == column[-1] or high == [0, 0]:
        keep_going = False

print(warehouse)