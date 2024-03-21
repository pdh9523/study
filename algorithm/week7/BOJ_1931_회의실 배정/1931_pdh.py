import sys

schedule = [list(map(int, sys.stdin.readline().split())) for _ in range(int(input()))]
# 끝을 기준으로 정렬하고 끝 값이 짧으면 채택
schedule.sort(key = lambda x : (x[1],x[0]))
# schedule.sort(key = lambda x : (x[1]))  <<< 틀림. 왜? 끝 기준인데 같은 경우 앞도 정렬되야 함. 그래서 x[0] 도 후순위 정렬이 필요

end = 0
count = 0

for start_time, end_time in schedule:
    if end <= start_time :
        count += 1
        end = end_time

print(count)