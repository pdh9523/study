# w, h = map(int, input().split())  # 격자 크기
# p, q = map(int, input().split())  # 초기 좌표 값
# t = int(input())  # 개미가 움직일 시간
#
# dx = [-1, -1, 1, 1]  # 개미의 x 방향 이동 (대각선)
# dy = [1, -1, -1, 1]  # 개미의 y 방향 이동 (대각선)
#
# arr = [[0] * (w + 1) for _ in range(h + 1)]  # 격자 초기화
#
# x, y = h - q, p  # 초기 위치 설정
# dir = 0  # 초기 방향 설정 (오른쪽 위)
#
# arr[x][y] = 1  # 시작 위치에 개미 번호 설정
# count = 1  # 개미의 이동 순서
#
# while t+2 > 0:
#     nx = x + dx[dir]
#     ny = y + dy[dir]
#
#     if 0 <= nx <= h and 0 <= ny <= w and arr[nx][ny] == 0:
#         count += 1
#         t -= 1
#         arr[nx][ny] = count
#         x, y = nx, ny
#     else:
#         if ny == w and dir == 0:
#             dir = 1
#         elif nx == 0 and dir == 1:
#             dir = 2
#         elif nx == h and dir == 2:
#             dir = 1
#         elif ny == 0 and dir == 1:
#             dir = 0
#         elif nx == 0 and dir == 0:
#             dir = 3
#         elif ny == w and dir == 3:
#             dir = 2
#         t -= 1
# for row in arr:
#     print(*row)

w, h = map(int, input().split())  # 격자 크기
p, q = map(int, input().split())  # 초기 좌표 값
t = int(input())  # 개미가 움직일 시간

dx = [-1, -1, 1, 1]  # 개미의 x 방향 이동 (대각선)
dy = [1, -1, -1, 1]  # 개미의 y 방향 이동 (대각선)

arr = [[0] * (w + 1) for _ in range(h + 1)]  # 격자 초기화

x, y = h - q, p  # 초기 위치 설정
dir = 0  # 초기 방향 설정 (오른쪽 위)

arr[x][y] = 1  # 시작 위치에 개미 번호 설정
count = 1  # 개미의 이동 순서

while t > 0:
    nx = x + dx[dir]
    ny = y + dy[dir]

    # 다음 위치가 격자 범위 안에 있는지 확인
    if 0 <= nx < h and 0 <= ny < w:
        # 격자 범위 안에 있을 때만 값을 할당하고 개미 이동
        count += 1
        t -= 1
        arr[nx][ny] = count
        x, y = nx, ny
    else:
        # 만약 다음 위치가 격자 범위를 벗어나면 개미가 방향을 바꾸도록 합니다.
        # 이 경우에는 count를 증가시키지 않고 개미의 위치만 변경합니다.
        if nx < 0 or nx >= h:
            dx[dir] *= -1  # x 방향 반전
        if ny < 0 or ny >= w:
            dy[dir] *= -1  # y 방향 반전
        dir = (dir + 1) % 4  # 방향 변경
        x, y = x + dx[dir], y + dy[dir]  # 다음 위치로 개미 이동

# 최종 결과 출력
for row in arr:
    print(*row)



for row in arr:
    print(*row)



