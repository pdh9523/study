# def dfs(start_x, start_y):
#     global d
#     global cnt
    
#     if arr[start_x][start_y] == 0: # 청소
#         arr[start_x][start_y] = 2
#         cnt += 1

#     for k in range(4):
#         nx = start_x + dx[k]
#         ny = start_y + dy[k]
#         if arr[nx][ny] == 0 and 0 <= nx < N and 0 <= ny < M:
#             d -= 1
#             if d < 0:
#                 d = 3
#             if d == 0 and arr[start_x-1][start_y] == 0:
#                 arr[start_x-1][start_y] = 2
#                 next_x = start_x - 1
#                 next_y = start_y
#                 cnt += 1
#                 dfs(next_x, next_y)
#             elif d == 1 and arr[start_x][start_y+1] == 0:
#                 arr[start_x][start_y+1] = 2
#                 next_x = start_x
#                 next_y = start_y+1
#                 cnt += 1
#                 dfs(next_x, next_y)
#             elif d == 2 and arr[start_x+1][start_y] == 0:
#                 arr[start_x+1][start_y] = 2
#                 next_x = start_x+1
#                 next_y = start_y
#                 cnt += 1
#                 dfs(next_x, next_y)
#             elif d == 3 and arr[start_x][start_y-1] == 0:
#                 arr[start_x][start_y-1] = 2
#                 next_x = start_x
#                 next_y = start_y-1
#                 cnt += 1
#                 dfs(next_x, next_y)
    
#     if 0 <= start_x+1 < N and 0 <= start_x-1 < N and 0 <= start_y+1 < M and 0 <= start_y-1 < M and (arr[start_x+1][start_y] == arr[start_x-1][start_y] == arr[start_x][start_y+1] == arr[start_x][start_y-1] == 1 or arr[start_x+1][start_y] == arr[start_x-1][start_y] == arr[start_x][start_y+1] == arr[start_x][start_y-1] == 2):
#         if d == 0 and arr[start_x+1][start_y] != 1:
#             next_x = start_x+1
#             next_y = start_y
#             dfs(next_x, next_y)
#         elif d == 0 and arr[start_x+1][start_y] == 1:
#             return cnt
#         elif d == 1 and arr[start_x][start_y-1] != 1:
#             next_x = start_x
#             next_y = start_y-1
#             dfs(next_x, next_y)
#         elif d == 1 and arr[start_x][start_y-1] == 1:
#             return cnt
#         elif d == 2 and arr[start_x-1][start_y] != 1:
#             next_x = start_x-1
#             next_y = start_y
#             dfs(next_x, next_y)
#         elif d == 2 and arr[start_x-1][start_y] == 1:
#             return cnt
#         elif d == 3 and arr[start_x][start_y+1] != 1:
#             next_x = start_x
#             next_y = start_y+1
#             dfs(next_x, next_y)
#         elif d == 3 and arr[start_x][start_y+1] == 1:
#             return cnt

# N, M = map(int, input().split()) # 방의 크기 N과 M
# r, c, d = map(int, input().split()) # 로봇 청소기의 처음 좌표 및 바라보는 방향
# # d = 0 북, 1 동, 2 남, 3 서
# arr = [list(map(int, input().split())) for _ in range(N)] # 청소되지 않은 빈 칸

# cnt = 0
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# start_x, start_y = r, c

# print(dfs(start_x, start_y))
def clean_room(arr, start_x, start_y, start_d):
    cnt = 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북, 동, 남, 서
    
    def valid(x, y):
        return 0 <= x < N and 0 <= y < M

    def dfs(x, y, d):
        nonlocal cnt
        if arr[x][y] == 0:
            arr[x][y] = 2
            cnt += 1

        for _ in range(4):
            d = (d + 3) % 4  # 왼쪽으로 회전
            nx, ny = x + directions[d][0], y + directions[d][1]
            if valid(nx, ny) and arr[nx][ny] == 0:
                dfs(nx, ny, d)
                return  # 한 칸 전진한 후, 다시 회전할 필요가 없으므로 반환

        # 네 방향 모두 청소가 되어있거나 벽인 경우
        back_x, back_y = x - directions[d][0], y - directions[d][1]
        if valid(back_x, back_y) and arr[back_x][back_y] != 1:
            dfs(back_x, back_y, d)  # 후진
        else:
            return

    dfs(start_x, start_y, start_d)
    return cnt


N, M = map(int, input().split())  # 방의 크기 N과 M
r, c, d = map(int, input().split())  # 로봇 청소기의 처음 좌표 및 바라보는 방향
# d = 0 북, 1 동, 2 남, 3 서
arr = [list(map(int, input().split())) for _ in range(N)]  # 청소되지 않은 빈 칸

print(clean_room(arr, r, c, d))
