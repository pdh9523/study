# def simulate_inning(start_i, start_j):
#     global score
#     out = 0
#     hit = 0
#     for i in range(start_i, N):
#         for j in range(start_j, 9):
#             if arr[i][j] == 0:  # 아웃
#                 out += 1
#                 if out == 3:
#                     return simulate_inning(i+1, j+1) # 다음 이닝의 시작 인덱스와 초기화된 아웃 수 반환
#             else:
#                 hit += arr[i][j]
#                 if hit >= 4:
#                     score += 1
#                     hit -= 4
                
#     return score  # 모든 이닝을 돌았을 때 반환

# N = int(input())  # 이닝 수
# arr = [list(map(int, input().split())) for _ in range(N)]  # 선수들의 결과

# # 1번이 무조건 4번 타순
# for i in range(N):
#     arr[i][0], arr[i][3] = arr[i][3], arr[i][0]

# score = 0
# start_i, start_j = 0, 0  # 경기 시작
# score = simulate_inning(start_i, start_j)
# print(score)  # 결과 출력

# permutations, 시간초과남
# import sys
# from itertools import permutations

# def simulate_inning(order, inning_results):
#     score = 0
#     player = 0
#     for inning in inning_results:
#         outs = 0
#         bases = [0] * 4
#         while outs < 3:
#             result = inning[order[player]]
#             if result == 0:
#                 outs += 1
#             else:
#                 for i in range(3, -1, -1):
#                     if bases[i]:
#                         if i + result >= 4:
#                             score += 1
#                             bases[i] = 0
#                         else:
#                             bases[i + result] = 1
#                             bases[i] = 0
#                 if result < 4:
#                     bases[result] = 1
#                 else:
#                     score += sum(bases) + 1
#                     bases = [0] * 4
#             player = (player + 1) % 9
#     return score

# def solve(N, inning_results):
#     max_score = 0
#     for order in permutations(range(1, 9), 8):
#         order = list(order[:3]) + [0] + list(order[3:])
#         score = simulate_inning(order, inning_results)
#         max_score = max(max_score, score)
#     return max_score


# N = int(input())  # 이닝 수
# inning_results = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]  # 각 이닝에서의 결과
# print(solve(N, inning_results))

import sys
from itertools import permutations
N = int(sys.stdin.readline())
game = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 조건
# 1. 한 이닝에 3아웃이 발생하면 이닝 종료
# 2. 9번 타자까지 공을 쳤는데 3아웃이 발생하지 않으면 이닝 종료하지않음
# 3. 1번 이닝에서 6번 타자가 마지막이면 2번 이닝은 7번 타자부터 시작
# 4. 경기가 시작하기 전에 타순을 정해줘야함, 단 4번타자는 고정 1번 선수
order = [i for i in range(1,9)] # 고정된 4번타자 제외하고 순서를 정해주자.
result = 0
for x in permutations(order,8): # 8명의 순서의 조합을 따져본다.
    x = list(x)
    batter = x[:3] + [0] + x[3:] # 4번 조건. 1~3번 타자(랜덤 3명) / 1번 선수 (1번 선수) / 4~8번 타자(랜덤 5명)
    number, point = 0, 0 # 타수와 점수
    for i in range(N): # 각 이닝에 대해
        out = 0 #이닝이 돌면 out은 0으로 초기화
        p1 = p2 = p3 = 0 # 1~3루의 현재 상태
        while out < 3: # 1번, 2번 조건. out이 3번이 되기 전까지 반복
            #여기서부터 야구 룰
            if game[i][batter[number]] == 0:
                out += 1 
            elif game[i][batter[number]] == 1: 
                point += p3 
                p1, p2, p3 = 1, p1, p2
            elif game[i][batter[number]] == 2: 
                point += p2 + p3 
                p1, p2, p3 = 0, 1, p1
            elif game[i][batter[number]] == 3:
                point += p1 + p2 + p3
                p1, p2, p3 = 0, 0, 1
            elif game[i][batter[number]] == 4:
                point += p1 + p2 + p3 + 1
                p1, p2, p3 = 0, 0, 0
            number += 1 # 타순 증가
            if number == 9: #타순이 9가 되면
                number = 0 #다시 0으로 초기화
    # 3번 조건. 이닝이 끝나도 number을 초기화 하지 않으므로 다음이닝에 타순 유지
    result = max(result, point)
print(result)











