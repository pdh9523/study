# 한수 => 양의 정수X의 각 자리 수가 등차수열 ex) 246
N = int(input())
# 1000이하의 자연수, 1000은 한수가 아니므로 3자리 숫자만 탐색하면됨
# 한자리, 두자리의 자연수는 다 한 수임. 즉 N = 100 이라면 한수의 갯수는 99
hansu = []
result = 0
for i in range(N + 1):
    
    alpha = i // 100 # 백의자리수
    beta = (i // 10) % 10 # 십의 자리수
    gamma = i % 10 # 일의 자리수
        
    if alpha - beta == beta - gamma and alpha != 0:
        hansu.append(i)

if N >= 100:        
    result = len(hansu) + 99
    print(result)
else:
    print(N)