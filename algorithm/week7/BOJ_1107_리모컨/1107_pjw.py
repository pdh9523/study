def is_possible(num, broken): # 고장 버튼 판단
    num_str = str(num)
    for digit in num_str:
        if digit in broken:
            return False
    return True

def count_press(N, broken):
    min_press = abs(N - 100)  # 현재 채널은 100번
    for channel in range(1000001):  # 채널은 0~ 50만이지만, 범위를 50만으로 설정하면 
        # 50만 tk에서 50만보다 큰 채널에서 내려오는게 안먹음
        if is_possible(channel, broken):  # 이동 가능한 채널인 경우
            min_press = min(min_press, abs(N - channel) + len(str(channel)))  # 현재까지의 최소 횟수와 새로운 채널까지의 횟수를 비교하여 갱신
    return min_press

N = int(input())  # 이동하려는 채널
M = int(input())  # 고장난 버튼의 개수
broken = set(input().split()) if M > 0 else set()  # 고장난 버튼 집합. 없으면 빈 집합으로 초기화

result = count_press(N, broken)
print(result)
