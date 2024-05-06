for _ in range(int(input())):
    N = int(input())
    arr = input().split()
    ans = ""
    for char in arr :
        if ans and ans[0] >= char :
            # 앞에 붙이거나
            ans = char + ans
        else :
            # 뒤에 붙이거나
            ans = ans + char
    print(ans)