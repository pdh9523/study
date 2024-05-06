# 하노이탑 조건 없으면?
# 그냥 오른쪽에 하나 세운다 치고 필요한거 1,2 번갈아서 나올때까지 옮기면 됨

N = int(input())

hanoi = [[*map(int,input().split())],[],[]]
ans = []
for num in range(N,0,-1):
    for i in range(2):

        if num in hanoi[i]:

            while hanoi[i][-1] != num:
                hanoi[1-i].append(hanoi[i].pop())
                ans.append((i+1, 2-i))

            hanoi[2].append(hanoi[i].pop())
            ans.append((i+1, 3))
print(len(ans))
for a in ans:
    print(*a)
