import sys

input = sys.stdin.readline


N = int(input())
stack = []
ans = 0  
for _ in range(N):
    task, *info = map(int,input().split())
    # 1이면 할일 쌓아주기
    if task == 1 :
        stack.append(list(info))
    
    # 할일 수행
    if stack :
        # 스택의 맨 위의 일을 1분 하고
        stack[-1][1] -= 1
        # 일이 0분 남았으면
        if stack[-1][1] == 0 :
            # 점수를 ans에 더함
            ans += stack.pop()[0]
print(ans)