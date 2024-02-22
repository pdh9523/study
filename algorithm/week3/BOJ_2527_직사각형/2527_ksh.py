for t in range(4):
    rec = list(map(int, input().split()))

    fir = rec[:4]   # 첫번째 사각형
    sec = rec[4:]   # 두번째 사각형

    if fir[2] < sec[0] or sec[2] < fir[0]:        # 사각형의 x 좌표가 안 겹칠 때
        print('d')
    elif fir[2] == sec[0] or fir[0] == sec[2]:    # 사각형의 x 좌표가 겹칠 때
        if fir[3] == sec[1] or fir[1] == sec[3]:  # 세로도 겹치면 점
            print('c')
        elif fir[3] < sec[1] or sec[3] < fir[1]:  # 안 겹치면 공통부분 없음
            print('d')
        else:                                     # 그 외의 경우 선분
            print('b')
    else:                                         # 사각형이 x 축으로 범위로 겹칠 때
        if fir[3] == sec[1] or fir[1] == sec[3]:   # 세로가 겹치면 선분
            print('b')
        elif fir[3] < sec[1] or sec[3] < fir[1]:  # 안 겹치면 공통부분 없음
            print('d')
        else:                                     # 그 외의 경우 직사각형
            print('a')
