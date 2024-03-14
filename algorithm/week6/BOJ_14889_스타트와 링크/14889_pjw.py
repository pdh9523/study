from itertools import combinations # 조합 씁시다

def cal_score(team):
    score = 0
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            score += arr[team[i]][team[j]] + arr[team[j]][team[i]]
    return score

N = int(input())  # 사람 수
arr = [list(map(int, input().split())) for _ in range(N)]  # 능력치

all_members = set(range(N))  # 전체 인원
min_diff = float('inf')  # 최솟값

for team_a in combinations(range(N), N // 2): # 가능한 조합들 다 찾기
    team_b = list(set(range(N)) - set(team_a))  

    score_a = cal_score(team_a)  
    score_b = cal_score(team_b)  

    min_diff = min(min_diff, abs(score_a - score_b))  # 계속 최솟값 비교해서
# 제일 작은 값 찾기
print(min_diff)