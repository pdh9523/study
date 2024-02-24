# 별4 동3 네2 세1
import sys

t = int(input())

for _ in range(t):
    a = list(map(int,sys.stdin.readline().strip().split()))[1:] # 리스트 맨 앞은 개수를 나타냄

    b = list(map(int,sys.stdin.readline().strip().split()))[1:]

    for i in range(4,0,-1):             # 우선순위 4 3 2 1 순으로 순회하면서
        if a.count(i) > b.count(i) :    # 결판이 났으면 출력하고 break
            print("A")
            break
        elif a.count(i) < b.count(i) :
            print("B")
            break
    else :
        print("D")                      # break 없이 순회를 완료 했다면 무승부