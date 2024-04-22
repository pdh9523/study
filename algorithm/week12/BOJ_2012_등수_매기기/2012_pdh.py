import sys
input = sys.stdin.readline

N = int(input())
# 원하는 등수 정렬
students = sorted([ int(input()) for _ in range(N)])
# 정렬하고 range를 빼서 나온 절대값을 더하기
print(sum(map(lambda x : abs(students[x] - (x+1)), range(N))))
