# [3 - 단순 순회 + zip(dictionary) | pypy3 111108KB, 448ms | python3 31120KB, 776ms]

import sys
input = sys.stdin.readline

N = int(input())
right = list(map(str, input().split()))
wrong_d = dict(zip(input().split(), range(N)))

cnt = 0
for i in range(N-1):
    for j in range(i+1, N):
        if wrong_d[right[i]] < wrong_d[right[j]]:
            cnt += 1

print(f'{cnt}/{int(N * (N-1) / 2)}')



'''
[1 - combinations + dictionary | pypy3 268612KB, 868ms | python3 256568KB, 1100ms]

import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
right = list(map(str, input().split()))
wrong = list(map(str, input().split()))

right_c = list(combinations(right, 2))

wrong_d = {}
for i in range(N):
    wrong_d[wrong[i]] = i

cnt = 0
for first, last in right_c:
    if wrong_d[first] < wrong_d[last]:
        cnt += 1

print(f'{cnt}/{int(N * (N-1) / 2)}')
'''



'''
[2 - 단순 순회 + dictionary | pypy3 111108KB, 444ms | python3 31120KB, 772ms]

import sys
input = sys.stdin.readline

N = int(input())
right = list(map(str, input().split()))
wrong = list(map(str, input().split()))

wrong_d = {}
for i in range(N):
    wrong_d[wrong[i]] = i

cnt = 0
for i in range(N-1):
    for j in range(i+1, N):
        if wrong_d[right[i]] < wrong_d[right[j]]:
            cnt += 1

print(f'{cnt}/{int(N * (N-1) / 2)}')
'''



'''
[1 - 메모리 초과]

import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
right = list(map(str, input().split()))
wrong = list(map(str, input().split()))

right_c = list(combinations(right, 2))
wrong_c = list(combinations(wrong, 2))

cnt = 0
for i in range(len(right_c)):
    if right_c[i] in wrong_c:
        cnt += 1

print(f'{cnt}/{int(N * (N-1) / 2)}')
'''



'''
[2 - 시간 초과]

import sys
input = sys.stdin.readline

N = int(input())
right = list(map(str, input().split()))
wrong = list(map(str, input().split()))

right_d, wrong_d = {}, {}
for i in range(N):
    for j in range(N):
        if i < j:
            if right[i] in right_d.keys():
                right_d[right[i]].append(right[j])
            else:
                right_d[right[i]] = [right[j]]
            if wrong[i] in wrong_d.keys():
                wrong_d[wrong[i]].append(wrong[j])
            else:
                wrong_d[wrong[i]] = [wrong[j]]

cnt = 0
for i in range(N-1):
    if right[i] in wrong_d.keys():
        arr = right_d[right[i]]
        for k in range(len(right_d[right[i]])):
            if arr[k] in wrong_d[right[i]]:
                cnt += 1

print(f'{cnt}/{int(N * (N-1) / 2)}')
'''



'''
[3 - 시간 초과]

import sys
input = sys.stdin.readline

N = int(input())
right = list(map(str, input().split()))
wrong = list(map(str, input().split()))

cnt = 0
for i in range(N):
    w_idx = wrong.index(right[i])
    for j in range(i+1, N):
        w_temp = wrong[w_idx+1:]
        if right[j] in w_temp:
            cnt += 1

print(f'{cnt}/{int(N * (N-1) / 2)}')
'''



'''
[4 - 시간 초과]

import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
right = list(map(str, input().split()))
wrong = list(map(str, input().split()))

right_c = list(combinations(right, 2))

cnt = 0
for first, last in right_c:
    if wrong.index(first) < wrong.index(last):
        cnt += 1

print(f'{cnt}/{int(N * (N-1) / 2)}')
'''