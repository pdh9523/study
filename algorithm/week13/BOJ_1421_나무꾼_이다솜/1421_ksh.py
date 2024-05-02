'[Python3 31120KB, 1872ms | PyPy3 110752KB, 176ms]'

import sys
input = sys.stdin.readline

N, C, W = map(int, input().split())        # 나무의 개수 N, 나무를 자를 때 드는 비용 C, 나무 한 단위의 가격 W
woods = [int(input()) for _ in range(N)]   # 나무의 길이

woods.sort()
max_revenue = 0
for cutting_length in range(1, woods[-1] + 1):   # 나무를 1부터 가장 긴 나무 도막의 길이만큼으로 순회하며 자르는 경우를 계산한다.
    revenue = 0
    for i in range(N):
        cutting_cnt = woods[i] // cutting_length
        if woods[i] % cutting_length == 0:
            cutting_cnt -= 1
        max_part_revenue = 0
        for k in range(cutting_cnt + 1):
            cost = k * C
            if k == 0 and woods[i] != cutting_length:
                part_revenue = 0
            else:
                part_revenue = cutting_length * k * W - cost
                if k == cutting_cnt and woods[i] % cutting_length == 0:
                    part_revenue += cutting_length * W
            if part_revenue > max_part_revenue:
                max_part_revenue = part_revenue
        revenue += max_part_revenue
    if revenue > max_revenue:
        max_revenue = revenue

print(max_revenue)