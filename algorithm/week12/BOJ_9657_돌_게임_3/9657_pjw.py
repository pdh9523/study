N = int(input()) # 돌게임
# 선턴 SK, 후턴 CY
dp = [0] * (N+1) # 디피, 디피에 담기는 것? N일때 0까지 소모시킬 수 있는 횟수

# N개의 돌 중 1, 3, 4개씩 빼면서 가져갈 수 있음
# 0번 인덱스를 N개의 돌로 놓고, N번 인덱스를 돌이 0이되는 걸로, dp에 담긴 수의 홀짝으로 승패 판단
for i in range(1, N+1):
    if i >= 1 and dp[i-1] == 0:
        dp[i] = 1
    elif i >= 3 and dp[i-3] == 0:
        dp[i] = 1
    elif i >= 4 and dp[i-4] == 0:
        dp[i] = 1
# dp = 1 => 1, 상근 승 dp = 2 => 2 창영 승 dp = 3 => 1 상근 승 dp = 4 => 1 상근 승 
# dp = 5 => 3, 상근 승 dp = 6 => 3 상근 승 dp = 7 => 4 창영 승 dp = 8 => 5 상근 승
# dp = 9 => 상근 승
if dp[N] == 1:
    print('SK')
else:
    print('CY')