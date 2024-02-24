t = int(input())
cnt = 0
result = [0]
for i in range(t//2,t+1):       # 반으로 지정한 이유 : 어차피 반 이하로 설정하면 2방컷
    test_list = [t,i]

    while True :
        next = test_list[-2]-test_list[-1]  # 문제 설명 그대로 뒤에서 2번째 - 뒤에서 1번째 빼서 next 를 만들고
        
        # next 가 0 이상이면 append
        if next >= 0 :              
            test_list.append(next)
        # next가 0 이하면 종료
        else :
            # cnt로 최대값을 설정해 그것보다 큰 경우에만 result에 만들어진 리스트를 저장
            if len(test_list) > cnt :
                result = test_list[:]
                cnt = len(result)
                break
            else :
                break
print(cnt)
print(*result)