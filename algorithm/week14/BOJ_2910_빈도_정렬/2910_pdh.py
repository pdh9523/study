N,C = map(int,input().split())
arr = [*map(int,input().split())]

result = dict()
for num in arr :
    result[num]=result.get(num,0)+1
# result의 key,value를 value 기준으로 내림차순 정렬 (여기서 x[0]도 후순위 정렬하는 경우 순서에서 문제생김)
ans = sorted(result.items(), key=lambda x : x[1], reverse=True)

for k,v in ans :
    for _ in range(v):
        print(k, end=" ")