from itertools import combinations # 유찬쌤 방법 써보기

a, b = map(int,input().split())

test_list = list(map(int,input().split()))

result = list(map(sum,(list(combinations(test_list,3))))) #result에 아무튼 우겨넣었습니다.

min = 1e1000 # 대충 큰 수
min_value = 0 # 작은값인지 비교

for item in result :
    if 0 <= b-item < min : # 작으면 ?
        min = b-item # 담는다.
        min_value = item
print(min_value)