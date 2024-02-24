import sys
from math import ceil
input = sys.stdin.readline


N,K = map(int,input().split())

man = [0] * 7                                   # 남자
woman = [0] * 7                                 # 여자

for _ in range(N):
    gen,grade = map(int,input().split())
    if gen == 0 :
        man[grade] += 1                         # 학년을 리스트 인덱스로 활용
    elif gen == 1 :
        woman[grade] += 1

result = sum(map(lambda x : ceil(x/K), man)) + sum(map(lambda x : ceil(x/K), woman))    # x/k를 올림하여 합계를 계산

print(result)