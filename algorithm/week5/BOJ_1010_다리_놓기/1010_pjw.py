T = int(input())
'''
다리만들기 이거 경우의 수
M! /(M-N)!*N! 

'''
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # 각각 서쪽과 동쪽 사이트 갯수
    n1 = 1
    for i in range(M):
        n1 *= i+1
    n2 = 1
    for j in range(M-N):
        n2 *= j+1
    n3 = 1
    for k in range(N):
        n3 *= k+1

    print(int(n1/(n2*n3)))