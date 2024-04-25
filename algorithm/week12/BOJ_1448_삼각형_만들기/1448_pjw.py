# from itertools import combinations

# def max_return(arr):
#     max_sum = -1
#     for combination in combinations(arr, 3):
#         max_num = max(combination)
#         other = [num for num in combination if num != max_num ]
        
#         # 가장 큰 수가 2개 이상일 경우에는 나머지 두 수로 삼각형을 형성
#         if len(other) > 1:
#             max_square = max_num**2
#             other_square_sum = other[0]**2 + other[1]**2
#             if max_square > other_square_sum:
#                 continue
#             else:
#                 cur_sum = sum(other) + max_num
#                 if cur_sum > max_sum:
#                     max_sum = cur_sum
#                     max_com = combination
#         else:
#             max_square = max_num**2
#             other_square_sum = other[0]**2 + max_num**2
#             if max_square > other_square_sum:
#                 continue
#             else:
#                 cur_sum = sum(other) + max_num*2
#                 if cur_sum > max_sum:
#                     max_sum = cur_sum

#     return max_sum

N = int(input()) # 빨대 개수
arr = [int(input()) for _ in range(N)] # 한 줄에 빨대 1개

arr.sort(reverse=True)
for i in range(N):
    try:
        if arr[i] >= arr[i+1] + arr[i+2]:
            continue
        else:
            result = arr[i]+arr[i+1]+arr[i+2]
            print(result)
            break
    except IndexError:
        print(-1)
        break
