N = int(input())

cnt_max = 0
max_i = 0
num = [[N] for _ in range(N + 1)]
for i in range(N//2, N + 1):    # 주어진 수의 절반 이상의 수를 순회하며 찾기
    cnt = 2                     # 첫번째 수와 마지막 수에 대하여 cnt 값 보정
    fir = N
    sec = i
    thr = i
    while fir - sec >= 0:       # 계산할 숫자가 음수가 아닐 때
        cnt += 1
        sec = fir - sec
        fir = thr
        thr = sec
        num[i].append(fir)
    num[i].append(sec)          # while 문 종료 후 마지막 숫자도 리스트에 append
    if cnt_max < cnt:           # cnt_max 업데이트
        cnt_max = cnt
        max_i = i
    elif cnt_max > cnt:         # 백트래킹 : cnt_max 값보다 cnt 가 작아지기 시작하면 반복문 중단
        break

print(cnt_max)
print(*num[max_i])