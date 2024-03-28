from collections import deque
import sys

def bfs(start, end):
    visited = [False] * 10000
    queue = deque([(start, "")])

    while queue:
        current, path = queue.popleft()
        if current == end:
            return path

        # D 연산
        next_num = (current * 2) % 10000
        if not visited[next_num]:
            visited[next_num] = True
            queue.append((next_num, path + "D"))

        # S 연산
        next_num = (current - 1) % 10000
        if not visited[next_num]:
            visited[next_num] = True
            queue.append((next_num, path + "S"))

        # L 연산
        next_num = current % 1000 * 10 + current // 1000
        if not visited[next_num]:
            visited[next_num] = True
            queue.append((next_num, path + "L"))

        # R 연산
        next_num = current % 10 * 1000 + current // 10
        if not visited[next_num]:
            visited[next_num] = True
            queue.append((next_num, path + "R"))


T = int(input())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().strip().split())
    result = bfs(A, B)
    print(result)
