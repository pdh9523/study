# # 색종이 범위 함수
# def is_valid(x, y, size, board):
#     for i in range(x, x+size):
#         for j in range(y, y+size):
#             if i >= 10 or j >= 10 or board[i][j] == 0:
#                 return False
    
#     return True

# # 덮기
# def cover(x, y, size, board, value):
#     for i in range(x, x+size):
#         for j in range(y, y+size):
#             board[i][j] = value

# # 백트래킹
# def backtrack(x, y, board, cnt):
#     global min_cnt

#     if x == 9 and y == 9:
#         min_cnt = min(min_cnt, cnt)
#         return
    
#     if y == 9:
#         backtrack(x+1, 0, board, cnt) # 다음 줄 이동
#         return
    
#     if board[x][y] == 1:
#         for size in range(5, 0, -1):
#             if sizes[size] == 0 or x + size >= 10 or y + size >= 10:
#                 continue
#             if is_valid(x, y, size, board):
#                 cover(x, y, size, board, 0)  # 덮기
#                 sizes[size] -= 1 # 색종이 사용
#                 # print(x, y, sizes)
#                 backtrack(x, y+size, board, cnt+1) # 다음 칸
#                 cover(x, y, size, board, 1) # 색종이 제거
#                 sizes[size] += 1 # 색종이 원위치
                

#     else:
#         # 1이 아니다
#         backtrack(x, y+1, board, cnt)




# # 1이 적힌 모든 칸을 붙이는 데 필요한 색종이의 최소 개수
# # 경계 밖을 나가서도 안되고, 색종이끼리 겹쳐도 안됨, 1~5까지있음 5개씩있음
# # 0이 적힌 칸에는 색종이가 있으면 안됨
# arr = [list(map(int, input().split())) for _ in range(10)] # 10 * 10
# sizes = [0, 5, 5, 5, 5, 5] # 0~5 사이즈
# min_cnt = float('inf')
# backtrack(0, 0, arr, 0)

# if min_cnt == float('inf'):
#     print(-1)
# else:
#     print(min_cnt)

# import sys
# sys.stdin = open('input.txt')

# 색종이 범위 함수
def is_valid(x, y, size, board):
    for i in range(x, x + size):
        for j in range(y, y + size):
            if i >= 10 or j >= 10 or board[i][j] == 0:
                return False

    return True


# 덮기
def cover(x, y, size, board, value):
    for i in range(x, x + size):
        for j in range(y, y + size):
            board[i][j] = value


# 백트래킹
def backtrack(x, y, board, cnt):
    global min_cnt

    if x >= 10:  # 수정: 종료 조건 수정
        min_cnt = min(min_cnt, cnt)
        return

    if y >= 10:  # 수정: y의 범위 조건 변경
        backtrack(x + 1, 0, board, cnt)  # 다음 줄 이동
        return

    if board[x][y] == 1:
        for size in range(5, 0, -1):
            if sizes[size] == 0 or x + size > 10 or y + size > 10:  # 수정: 범위 검사 조건 수정
                continue
            if is_valid(x, y, size, board):
                cover(x, y, size, board, 0)  # 덮기
                sizes[size] -= 1  # 색종이 사용
                backtrack(x, y+size, board, cnt+1) # 다음 칸
                cover(x, y, size, board, 1)  # 색종이 제거
                sizes[size] += 1  # 색종이 원위치

    else:
        backtrack(x, y + 1, board, cnt)


# 1이 적힌 모든 칸을 붙이는 데 필요한 색종이의 최소 개수
arr = [list(map(int, input().split())) for _ in range(10)]  # 수정: 표준 입력으로 변경
sizes = [0, 5, 5, 5, 5, 5]  # 0~5 사이즈
min_cnt = float('inf')
backtrack(0, 0, arr, 0)

if min_cnt == float('inf'):
    print(-1)
else:
    print(min_cnt)

