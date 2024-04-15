for _ in range(int(input())):
    text=input()
    left=[]
    right=[]
    # 커서를 기준으로 [l e f t] | [r i g h t]
    for char in text :
        if char == ">":                         # 1. > 인 경우 : right 가 남아 있다면 right에서 left로 옮기기
            if right : left.append(right.pop())
        elif char == "<":                       # 2. < 인 경우 : left 가 남아 있다면 left에서 right로 옮기기
            if left : right.append(left.pop())
        elif char == "-":                       # 3. - 면 : left 가 남아있다면, left 하나씩 빼기
            if left : left.pop()
        else : left.append(char)                 # 그 외 : left에 입력

    print(*(left+right[::-1]), sep="")