N = int(input()) # 길이
arr = [list(map(int, input().split())) for _ in range(N)]
directions = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

def backtrack(flowers, depth, cost):
    global min_cost
    if depth == 3:
        min_cost = min(min_cost, cost)
        return
    
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            flower_cost = arr[i][j]
            skip = False
            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                if (nx, ny) in flowers:
                    skip = True
                    break
                flower_cost += arr[nx][ny]
            if not skip:
                flowers.add((i, j))
                temp = set(flowers)  # 현재 꽃을 심은 위치를 기록
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    flowers.add((nx, ny))
                backtrack(flowers, depth + 1, cost + flower_cost)
                flowers = temp  # 재귀 호출 후에 현재 꽃을 심은 위치로 복원

min_cost = float('inf')
backtrack(set(), 0, 0)
print(min_cost)
