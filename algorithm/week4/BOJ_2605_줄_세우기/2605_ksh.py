S = int(input())   # 학생의 수
numbers = list(map(int, input().split()))   # 학생들이 뽑은 번호

line = []
for i in range(S):
    line.insert(i-numbers[i], i + 1)

print(*line)



'''
# 동환

N = int(input()) # 학생수
number = list(map(int,input().split())) # 뽑는 번호표

result = []
for i in range(N):
    result.insert(number[i],i+1)
result.reverse()

print(*result)
'''