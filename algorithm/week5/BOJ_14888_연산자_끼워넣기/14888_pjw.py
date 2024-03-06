'''
N개의 수와 N-1개의 연산자가 주어졌을 때
연산자를 사용한 식에서 최대, 최솟값을 구하여라
유의 : 주어진 수의 위치를 바꿀 수 없음
연산은 연산 우선순위와는 상관없이 앞에서부터 진행

'''
n = int(input()) # 숫자갯수
numbers = list(map(int, input().split())) # 숫자 리스트
operators = list(map(int, input().split()))  # 연산자 개수: [+, -, *, //]

# 모든 연산자 조합 생성
op_combinations = []

def make_operators(index, cur_ops):
    if index == n - 1:
        op_combinations.append(cur_ops)
        return

    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            make_operators(index + 1, cur_ops + [i])
            operators[i] += 1

make_operators(0, [])
print(op_combinations)
# 최대값과 최소값 초기화
max_result = -1000000000
min_result = 1000000000

# 각 연산자 조합에 대해 계산
for ops in op_combinations:
    result = numbers[0]
    for i in range(n - 1):
        if ops[i] == 0:
            result += numbers[i + 1]
        elif ops[i] == 1:
            result -= numbers[i + 1]
        elif ops[i] == 2:
            result *= numbers[i + 1]
        elif ops[i] == 3:
            if result < 0:
                result = -(-result // numbers[i + 1])
            else:
                result //= numbers[i + 1]

    max_result = max(max_result, result)
    min_result = min(min_result, result)

# 결과 출력
print(max_result)
print(min_result)
