'21:11 ~ 21:17'

import sys
input = sys.stdin.readline

N = int(input())                            # 빨대의 수 N
length = [int(input()) for _ in range(N)]   # 빨대의 길이 정보

length.sort(reverse=True)

for i in range(N-2):
    if length[i] < length[i+1] + length[i+2]:
        exit(print(sum(length[i:i+3])))

print(-1)