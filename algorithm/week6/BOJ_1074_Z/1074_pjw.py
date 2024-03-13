def Z(r, c, N):
    if N == 0:
        return 0
    
    else:
        half = 2**(N-1)
        if r < half and c < half:
            return Z(r, c, N-1)
        elif r < half and c >= half:
            return half * half + Z(r, c-half, N-1)
        elif r >= half and c < half:
            return 2 * half * half + Z(r-half,c, N-1)
        else:
            return 3 * half * half + Z(r-half,c-half, N-1)

N, r, c = map(int, input().split()) # 행렬크기, r행 c열
# 몇번째로 방문했는지 찾기

print(Z(r, c, N))