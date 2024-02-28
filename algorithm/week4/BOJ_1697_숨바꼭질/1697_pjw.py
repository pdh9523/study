from collections import deque
# bfs는 신이다..
def find_min_time(N, K):
    visited = [False] * 100001  # 0~10만 => 10만1개
    queue = deque([(N, 0)])  # popleft 쓰고싶어요
    visited[N] = True

    while queue:
        current_pos, time = queue.popleft()

        if current_pos == K:  # 동생을 찾았을 때
            return time

        # 걷는 경우를 고려
        next_positions = [current_pos - 1, current_pos + 1, current_pos * 2]
        for next_pos in next_positions:
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))

    return -1  # 동생을 찾지 못한 경우

# 입력 처리
N, K = map(int, input().split()) # 수빈 위치, 동생 위치

# 결과 출력
print(find_min_time(N, K))

