N, K = map(int, input().split())   # N : 학생 수, K : 한 방에 배정할 수 있는 최대 인원
Students = [list(map(int, input().split())) for _ in range(N)]   # 성별 : 여자 0, 남자 1 / 학년

girl = [0] * 7   # 여학생 학년별 정보
boy = [0] * 7    # 남학생 학년별 정보
for S in Students:
    if S[0] == 0:   # 여학생이라면
        girl[S[1]] += 1
    else:           # 남학생이라면
        boy[S[1]] += 1

girl.pop(0)   # 주석 처리해도 무관하지만
boy.pop(0)    # index 보정을 위해서 넣은 0번째 원소 제거
everyone = girl + boy   # 방의 수를 계산할 때는 성별이 필요 없으므로 편의를 위해서 합치기

room = 0
for i in everyone:   # 그룹별 학생 수가 방의 최대 인원 수로
    if i % K == 0:   # 나누어 떨어지면
        room += i // K
    else:            # 나누어 떨어지지 않으면
        room += i // K + 1

print(room)