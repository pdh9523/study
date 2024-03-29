import sys
input = sys.stdin.readline
from itertools import combinations


N, S = map(int, input().split())        # N개의 정수, 정수 S
num = list(map(int, input().split()))   # N개의 정수

sum_S = 0
for k in range(1, N+1):
    part = list(combinations(num, k))   # k개의 원소를 가진 부분집합 구하기
    for p in part:                      # 부분집합을 순회하며
        if sum(p) == S:                 # 원소들의 합이 S인지 확인하고
            sum_S += 1                  # 결괏값 업데이트

print(sum_S)