def check():
    value = 0
    for i in range(N):
        candy = 0
        for j in range(N):
            if j == 0 :
                tmp = boards[i][j]
                candy += 1
            else :
                if tmp == boards[i][j]:
                    candy += 1
                else :
                    value = max(value,candy)
                    candy = 1
                    tmp = boards[i][j]
        value = max(value,candy)               
        if value == N :
            return N
    for j in range(N):
        candy = 0
        for i in range(N):
            if i == 0 :
                tmp = boards[i][j]
                candy += 1
            else :
                if tmp == boards[i][j]:
                    candy += 1
                else :
                    value = max(value,candy)
                    candy = 1
                    tmp = boards[i][j]
        value = max(value,candy)
        if value == N :
            return N
    return value 



N = int(input())

boards = [ list(input()) for _ in range(N) ]
ans = 0 
for i in range(N):
    for j in range(N):
        if 0 <= i+1 < N :
            boards[i+1][j], boards[i][j] = boards[i][j], boards[i+1][j]
            ans = max(ans,check())
            boards[i+1][j], boards[i][j] = boards[i][j], boards[i+1][j]
        if 0 <= j+1 < N :
            boards[i][j+1], boards[i][j] = boards[i][j], boards[i][j+1]
            ans = max(ans,check())
            boards[i][j+1], boards[i][j] = boards[i][j], boards[i][j+1]
print(ans)