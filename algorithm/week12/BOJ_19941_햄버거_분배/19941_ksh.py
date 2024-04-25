'20:53 ~ 21:09'

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
data = list(input())   # P : 사람, H : 햄버거

hamburger, people = [], []
for i in range(N):
    if data[i] == 'H':
        hamburger.append(i)
    else:
        people.append(i)

LH, LP, happy = len(hamburger), len(people), 0
for i in range(LP):       # 사람들이 순서대로 햄버거를 가져간다.
    if not hamburger:     # 햄버거가 없으면 남은 사람이 있어도 반복문을 종료한다.
        break
    for j in range(LH):   # 햄버거 목록을 순회하며 가져갈 수 있는 햄버거를 가져간다.
        if abs(people[i] - hamburger[j]) <= K:
            hamburger.pop(j)
            LH -= 1
            happy += 1
            break

print(happy)