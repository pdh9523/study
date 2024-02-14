# N : 카드의 수, M : 카드 3장의 합의 최댓값, cards : 카드 정보
N, M = map(int, input().split())
cards = list(map(int, input().split()))

# 카드를 순회하며 3장씩 더하고,
# 그 합이 M 이하인 수인 경우에 한하여
# 최댓값을 비교하며 구한다.
max_s = 0
for n in range(N):   # 첫번째 카드 - 한 카드를 세번 선택할 수 없으므로 한번 선택한 카드는 그 회차에서는 제거한다.
    s = 0                        # 해당 회차가 끝나면 다시 더해준다.
    s += cards[n]
    card1 = cards.pop(n)
    for i in range(N - 1):   # 두번째 카드
        s2 = s + cards[i]
        card2 = cards.pop(i)
        for j in range(N - 2):   # 세번째 카드
            s3 = s2 + cards[j]
            if max_s < s3 <= M:   # 해당 회차에서 구한 카드의 합이
                max_s = s3        # M 이하이면서 현재까지 구한 카드 3장의 합 중 최댓값보다 크면 최댓값을 재할당한다.
            s3 = s2
        s2 = s
        cards.insert(0, card2)
    cards.insert(0, card1)

# 결과 출력
print(max_s)