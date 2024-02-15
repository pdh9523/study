N = int(input())

# 한수 검증 함수
def f(N_list):
    if len(N_list) >= 2:
        X = []
        for i in range(1, len(N_list)):
            X.append(N_list[i] - N_list[i - 1])
        if X.count(X[0]) == len(X):
            return True
        else:
            return False
    else:
        return True

# 1부터 N 까지의 수가 한수인지 함수를 이용하여 검증하고 한수인 경우 카운트 
cnt = 0
for n in range(1, N + 1):
    N_list = list(map(int, list(str(n))))   # 함수 활용을 위해 수 자료형 변경

    result = f(N_list)
    if result == True:
        cnt += 1

# 결과 출력
print(cnt)