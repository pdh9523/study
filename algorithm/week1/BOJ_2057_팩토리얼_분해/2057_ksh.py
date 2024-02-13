N = int(input())

squares = [1]
pac = 1
if N >= 1:
    for n in range(1, N):
        pac *= n
        if pac > N:
            break
        squares.append(pac)

# 부분합 구하기
for i in range(1 << len(squares)):
    part = []
    for j in range(len(squares)):
        if i & (1 << j):
            part.append(squares[j])
    if sum(part) == N and N != 0:   # 부분합과 N이 같으면 결과 출력 및 코드 중지
        print('YES')
        break

else:   # 부분합 중 N과 동일한 것이 없으면 결과 출력
    print('NO')