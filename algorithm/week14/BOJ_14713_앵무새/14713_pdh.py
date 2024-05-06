from collections import deque

N = int(input())

text_list = []
for _ in range(N):
    text_list.append(deque(input().split()))

target = deque(input().split())
ans = "Possible"

while target :
    t = target.popleft() 

    # 앵무새가 말한 리스트를 순회하면서 맨 앞에 target이 순서대로 나오는지 확인 
    for i in range(N) :
        if text_list[i] and text_list[i][0] == t :
            # 있으면 없애고 계속 순회
            text_list[i].popleft()
            break
    else :
        ans = "Impossible"
        break

# 말이 남아 있으면 
if any(text_list) :
    ans = "Impossible"

print(ans)