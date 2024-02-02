# 입력값 받기
N = int(input())
XYs = [list(map(int, input().split())) for _ in range(N)]

# sort 메서드로 정렬
XYs.sort()

# 언패킹으로 결과 출력
# 언패킹 대상이 2차원 배열임을 유의
for XY in XYs:
    print(*XY)