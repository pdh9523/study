N = int(input())
arr = [input() for _ in range(N)]

def gomgom(z):
    global count
    global empty
    for i in range(z, N):
        if arr[i] != 'ENTER' and arr[i] not in empty:
            empty.append(arr[i])
            count += 1
        elif arr[i] == 'ENTER':
            next_i = i+1
            empty = []
            return gomgom(next_i)
        elif arr[i] in empty:
            pass

    return count
empty = []
count = 0
print(gomgom(1))