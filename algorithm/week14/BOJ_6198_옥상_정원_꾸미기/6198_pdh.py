import sys

input = sys.stdin.readline


bd = [int(input()) for _ in range(int(input()))]
stack = []
ans = 0
# cnt가 스택의 크기가 됨 
cnt = 0
for i in bd :
    # 건물 높이 확인하면서
    while stack and stack[-1] <= i :
        # 낮은건 계속 팝
        stack.pop()
        cnt -=1
    
    stack.append(i)
    cnt += 1
    ans += cnt-1

print(ans)