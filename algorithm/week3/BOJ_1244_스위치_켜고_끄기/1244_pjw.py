N = int(input())
on_off = list(map(int, input().split()))
stu_num = int(input())
student = [list(map(int, input().split())) for _ in range(stu_num)]

# 스위치 상태 출력을 위한 변수 초기화
count = 0

for i in range(stu_num):
    if student[i][0] == 1:  # 남학생인 경우
        for j in range(N):
            if (j+1) % student[i][1] == 0:
                on_off[j] = 1 - on_off[j]  # 스위치 상태 변경
    else:  # 여학생인 경우
        k_arr = [0]  # k_arr 초기화
        k = 1
        while student[i][1] - k >= 1 and student[i][1] + k <= N and on_off[student[i][1] - k - 1] == on_off[student[i][1] + k - 1]:
            k_arr.append(k)
            k += 1
        alpha = max(k_arr)
        for l in range(student[i][1] - alpha - 1, student[i][1] + alpha):
            on_off[l] = 1 - on_off[l]  # 스위치 상태 변경

# 스위치 상태 출력
for state in on_off:
    print(state, end=' ')
    count += 1
    # 20개씩 출력 후 줄 바꾸기
    if count == 20:
        print()
        count = 0

# 마지막 줄이 20개 미만이면 한 번 더 줄 바꾸기
if count != 0:
    print()
