N = int(input())
room = [list(input()) for _ in range(N)]

# 전치행렬 이용하기 위해 원본 남겨두고 복사본 이용
room1 = room[:]

# 문자열 split 메서드와 문자열의 길이 이용
for n in range(N):
    room1[n] = ''.join(room1[n])
    room1[n] = room1[n].split('X')

cnt = 0
for n in range(N):
    for i in range(len(room1[n])):
        if len(room1[n][i]) >= 2:
            cnt += 1

print(cnt, end = ' ')

# 전치행렬 생성
room2 = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        room2[i][j] = room[j][i]

for n in range(N):
    room2[n] = ''.join(room2[n])
    room2[n] = room2[n].split('X')

cnt = 0
for n in range(N):
    for i in range(len(room2[n])):
        if len(room2[n][i]) >= 2:
            cnt += 1

print(cnt)





'''
# 누울 수 있는 행과 열의 수 구하기

N = int(input())
room = [list(input()) for _ in range(N)]

can1 = 0
for i in range(N):
    for j in range(N - 1):
        if room[i][j] == room[i][j + 1] == '.':
            can1 += 1
            break

can2 = 0
for j in range(N):
    for i in range(N - 1):
        if room[i][j] == room[i + 1][j] == '.':
            can2 += 1
            break

print(can1, can2)
'''