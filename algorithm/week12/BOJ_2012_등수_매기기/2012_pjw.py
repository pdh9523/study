N = int(input()) # 사람 수
arr = [int(input()) for _ in range(N)] # 예상 등수
# 불만도의 합을 최소화 하자 => 웬만하면 예상 등수와 같게 만들어 준다.

ant = []
for i in range(1, N+1):
    ant.append(i)
# print(ant)

result = 0
arr.sort()
for j in range(N):
    result += abs(ant[j] - arr[j])

print(result)