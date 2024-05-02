from itertools import combinations

N = int(input())

tastes = []
for _ in range(N):
    sour, bitter = map(int, input().split())
    tastes.append((sour, bitter))

min_dif = float('inf')
for r in range(1, N + 1):
    for selected in combinations(tastes, r):
        sour_product = 1
        bitter_sum = 0
        for taste in selected:
            sour_product *= taste[0]
            bitter_sum += taste[1]
        min_dif = min(min_dif, abs(sour_product - bitter_sum))

print(min_dif)
