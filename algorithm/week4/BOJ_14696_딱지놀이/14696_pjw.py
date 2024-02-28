# 라운드의 수 N 입력
N = int(input())

# 어린이 A와 B가 낸 딱지 정보 입력
arr = [list(map(int, input().split())) for _ in range(2 * N)]

# 어린이 A와 B가 낸 딱지 정보를 리스트에 따로 저장
a_st = []
b_st = []

for i in range(0, 2 * N-1, 2):  # 인덱스 1부터 시작하여 홀수번째 요소를 가져옴
    a_st.append(arr[i][1:])
    b_st.append(arr[i + 1][1:])

# N 라운드에 대한 딱지놀이 결과 계산
for a, b in zip(a_st, b_st):
    # 딱지의 각 모양의 개수 카운팅
    a_counts = [0] * 5
    b_counts = [0] * 5

    for sticker in a:
        a_counts[sticker-1] += 1

    for sticker in b:
        b_counts[sticker-1] += 1

    # 라운드 결과 계산
    winner = 'D'
    for i in range(4, 0, -1):
        if a_counts[i] > b_counts[i]:
            winner = 'A'
            break
        elif a_counts[i] < b_counts[i]:
            winner = 'B'
            break

    print(winner)


                    