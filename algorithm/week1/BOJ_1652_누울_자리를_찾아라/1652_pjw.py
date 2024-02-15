N = int(input())
arr = [list(map(str, input().strip())) for _ in range(N)]

count_guaro = 0
count_sero = 0
guaro = []
sero = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'X':
            guaro.append(j)
        guaro.sort()
        
        try:
            for i in guaro:
                alpha = abs(guaro[i] - guaro[i + 1])
                if alpha >= 2:
                    count_guaro += 1
                    guaro = []
        except IndexError:
            alpha = N - guaro[-1]
            if alpha >= 2:
                count_guaro += 1
                guaro = []
for j in range(N):
    for i in range(N):
        if arr[i][j] == 'X':
            sero.append(i)
        sero.sort()
        try:
            for i in sero:
                beta = abs(sero[i] - sero[i + 1])
                if beta >= 2:
                    count_sero += 1
                    sero = []
        except IndexError:
            beta = N - sero[-1]
            if beta >= 2:
                count_sero += 1
                sero = []
print(count_guaro , count_sero)