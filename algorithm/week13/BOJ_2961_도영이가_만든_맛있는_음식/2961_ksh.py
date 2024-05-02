'21:42 - 21:52 | Python3 31120KB, 40ms | PyPy3 109240KB, 112ms'

from itertools import combinations

N = int(input())
tastes = [list(map(int, input().split())) for _ in range(N)]

best_food = float('inf')
for i in range(1, N+1):
    foods = list(combinations(tastes, i))
    for food in foods:
        sour, bitter = 1, 0
        for k in range(len(food)):
            sour *= food[k][0]
            bitter += food[k][1]
        if best_food > abs(sour - bitter):
            best_food = abs(sour - bitter)

print(best_food)