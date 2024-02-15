def f(idx, current_sum, target_sum, arr):
    # 종료 조건: 현재 합이 목표 합과 일치하면 1을 반환하여 경우의 수를 세어줌
    if idx == len(arr):
        return 1 if current_sum == target_sum else 0

    # 숫자세기
    count = 0
    count += f(idx + 1, current_sum, target_sum, arr)  # 현재 원소를 포함시키지 않는 경우
    count += f(idx + 1, current_sum + arr[idx], target_sum, arr)  # 현재 원소를 포함시키는 경우
    return count

# 입력 받기
N, S = map(int, input().split())
arr = list(map(int, input().split()))

# 부분수열의 개수 계산
result = f(0, 0, S, arr)
if S == 0:
    result -= 1
print(result)

