arr = [input() for _ in range(36)] # 입력 받기
chess_map = [[0]*6 for _ in range(6)] # 빈 체스판 만들기(6*6)

if len(set(arr)) == 36: # arr의 길이
    for i in range(36):
        if i == 0: # 시작하면
            prev = arr[i] # 시작지점을 prev로 설정
            # ord는 유니코드 숫자로 바꿈, 즉 A는 65부터 시작
            x, y = ord(prev[0]) - 65, int(prev[1]) -1
            chess_map[x][y] = 1 # 시작점을 1로 바꿈
        elif 0 < i < 35: # 0~35까지
            now = arr[i] # now 설정
            x1, y1 = ord(now[0]) - 65, int(now[1]) - 1 # 이동한 지점 
            x2, y2 = ord(prev[0]) - 65, int(prev[1]) - 1 # 이동 전 지점

            dist = (((x2-x1) ** 2) + ((y2-y1) ** 2)) ** 0.5 # 나이트가 이동한 거리
            # 4+1의 제곱근이 이동거리, 가지 않았다면
            if dist == (5 ** 0.5) and chess_map[x1][y1] == 0:
                flag = 1 # flag를 1로 만든다(check 느낌)
                chess_map[x1][y1] = 1
                prev = now # 이제 이동한 지점이 이전 위치가 된다.
            else:
                flag = 0 # 위 조건에 부합하지 않는다면 실패
                break # 더 할 이유 없음
        else: # i == 36, 즉 도착
            now = arr[i]
            start_point = arr[0] # 시작지점에 갈 수 있느냐를 판별해야함
            # 아까랑 똑같음
            x1, y1 = ord(now[0]) - 65, int(now[1]) - 1
            x2, y2 = ord(start_point[0]) - 65, int(start_point[1]) - 1

            dist = (((x1-x2)**2) + ((y1-y2)**2))**0.5
            if dist == (5**0.5): # 거리 상 도달 가능하다면
                flag = 1 # flag = 1 
            else:
                flag = 0 # 아니면 못가는거
else:
    flag = 0 # 위 조건에 안걸리면 flag = 0

if flag == 1: # flag가 1이라면 갈 수 있는 거임
    print('Valid')
else: # 아니면 못감
    print('Invalid')