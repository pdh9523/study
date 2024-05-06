N = int(input())
txt = input()
ans, cnt = 0,0
for char in txt :
    # 괄호를 열거나 닫는게 쌓이는만큼 하루가 더 걸리는데
    if char == "(" :
        cnt += 1
    else :
        cnt -= 1
    # 절대값으로 ans를 갱신
    ans = max(ans,abs(cnt))

print(-1 if cnt else ans)