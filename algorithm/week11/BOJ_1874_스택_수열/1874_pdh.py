import sys


input = sys.stdin.readline

N = int(input())
stack = [] 
ans = [] 
cnt = 1 
for _ in range(N):
    num = int(input())          # 숫자를 입력받고

    while cnt <= num :          # 그 숫자가 카운트보다 높으면
        stack.append(cnt)       # 카운트를 그 수에 맞을 때 까지 스택에 넣음
        cnt += 1                
        ans.append("+")         # 스택에 넣으니까 + 
    
    if stack[-1] == num :       # 그 후, 스택 제일 위의 값이 숫자와 같다면
        stack.pop()             # 스택에서 팝
        ans.append("-")         # 스택에서 빼니까 -

    else :                      # 이 과정에서 문제가 생기면
        exit(print("NO"))       # 잘못된거니까 탈출

print(*ans, sep="\n")