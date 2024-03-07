knight = [input() for _ in range(36)]   # 입력 받은 자료
new_knight = [0] * 36                   # 정수형, index 보정 등의 재가공을 마친 자료
visited = [[0] * 6 for _ in range(6)]   # knight 가 방문한 칸의 정보를 담을 2차원 배열

for k in range(36):                     # 모든 정보를 순회하며 자료를 재가공하고, 방문한 칸을 표시
    if knight[k][0] == 'A':
        new_knight[k] = (int(knight[k][1]) - 1) * 10 + 0
    elif knight[k][0] == 'B':
        new_knight[k] = (int(knight[k][1]) - 1) * 10 + 1
    elif knight[k][0] == 'C':
        new_knight[k] = (int(knight[k][1]) - 1) * 10 + 2
    elif knight[k][0] == 'D':
        new_knight[k] = (int(knight[k][1]) - 1) * 10 + 3
    elif knight[k][0] == 'E':
        new_knight[k] = (int(knight[k][1]) - 1) * 10 + 4
    else:
        new_knight[k] = (int(knight[k][1]) - 1) * 10 + 5
    visited[new_knight[k]//10][new_knight[k]%10] = 1

for x in range(36):   # 모든 이동이 knight 가 할 수 있는 유효한 이동인지 확인
    i, j, p, q = new_knight[x]//10, new_knight[x]%10, new_knight[x-1]//10, new_knight[x-1]%10
    if (abs(p - i) == 1 or abs(p - i) == 2) and (abs(p - i) + abs(q - j) == 3):
        pass
    else:             # 만일 아니라면 코드 종료와 함께 'Invalid' 출력
        exit(print('Invalid'))

for v in visited:     # 모든 이동이 유효성 검사를 통과하였다면 모든 칸을 방문했는지 확인
    if v.count(1) != 6:
        print('Invalid')
        break
else:
    print('Valid')