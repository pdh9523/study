'21:24 - 21:41'

S = list(input())

zero_cnt = S.count('0') // 2
one_cnt = S.count('1') // 2

while one_cnt:
    S.pop(S.index('1'))
    one_cnt -= 1

i = len(S)-1
while zero_cnt:
    if S[i] == '0':
        S.pop(i)
        zero_cnt -= 1
    i -= 1

print(''.join(S))



'''
[25점]

print('0' * (zero_cnt//2) + '1' * (one_cnt//2))
'''