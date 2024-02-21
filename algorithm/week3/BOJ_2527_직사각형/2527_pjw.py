arr = [list(map(int, input().split())) for _ in range(4)]
for i in range(4):
    rect1 = arr[i][:4]
    rect2 = arr[i][4:]
    x1, y1, p1, q1 = rect1
    x2, y2, p2, q2 = rect2

    # 두 직사각형의 겹치는 영역을 구합니다.
    overlap_x1 = max(x1, x2)
    overlap_y1 = max(y1, y2)
    overlap_x2 = min(p1, p2)
    overlap_y2 = min(q1, q2)

    # 겹치는 영역의 너비와 높이를 구합니다.
    overlap_width = overlap_x2 - overlap_x1
    overlap_height = overlap_y2 - overlap_y1

    # 겹치는 영역이 없는 경우
    if overlap_width < 0 or overlap_height < 0:
        print('d')
    # 겹치는 영역이 점인 경우
    elif overlap_width == 0 and overlap_height == 0:
        print('c')
    # 겹치는 영역이 선분인 경우
    elif overlap_width == 0 or overlap_height == 0:
        print('b')
    # 겹치는 영역이 직사각형인 경우
    else:
        print('a')