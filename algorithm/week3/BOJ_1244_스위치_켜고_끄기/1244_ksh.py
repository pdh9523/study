N = int(input())                           # 스위치 개수
switch = [0] + list(map(int, input().split()))   # ON : 1, OFF : 0
S = int(input())                           # 학생 수
student = [list(map(int, input().split())) for _ in range(S)]   # [[성별, 수], [성별, 수], ...]

# 남학생 : 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
# 여학생 : 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서,
#        그 구간에 속한 스위치의 상태를 모두 바꾼다. 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.

for s in student:
    if s[0] == 1:   # 남학생
        for i in range(len(switch)):   # 스위치 순회
            if i % s[1] == 0:   # 스위치 번호가 남학생이 받은 수의 배수이면 스위치 상태 변환
                if switch[i] == 0:
                    switch[i] = 1
                else:
                    switch[i] = 0
    else:           # 여학생
        k = min(N - s[1], s[1] - 1)
        for j in range(k + 1):
            if switch[s[1] + j] == switch[s[1] - j]:   # 여학생이 받은 번호의 스위치를 기준으로 대칭이면 스위치 상태 변환
                if switch[s[1] + j] == 0:
                    switch[s[1] + j] = 1
                    switch[s[1] - j] = 1
                else:
                    switch[s[1] + j] = 0
                    switch[s[1] - j] = 0
            else:
                break

switch.pop(0)

# 스위치 정보 20개씩 출력
while switch:
    print(*switch[0:20])
    switch = switch[20:]