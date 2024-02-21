N, K = map(int, input().split())   # N : 온도를 측정한 전체 날짜의 수, K : 합을 구하기 위한 연속적인 날짜의 수
temp = list(map(int, input().split()))   # 온도

sum_t = sum(temp[: K])
sums = [sum_t]
for i in range(1, N - K + 1):   # 부분집합의 첫 원소 범위
    sum_t += temp[i + K - 1] - temp[i - 1]
    if temp[i - 1] < temp[i + K - 1]:   # 빠지는 원소와 더해지는 원소의 대소 비교
        sums.append(sum_t)

print(max(sums))



'''
시간 초과

max_t = sum(temp[: K])
for i in range(1, N - K + 1):   # 부분집합의 첫 원소 범위
    if temp[i - 1] < temp[i + K - 1]:
        if sum(temp[i : i + K]) > max_t:
            max_t = sum(temp[i : i + K])

print(max_t)
'''