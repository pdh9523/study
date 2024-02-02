# 리스트의 sort 메서드를 활용
# 내림차순 sort : list.sort(reverse = True)
N = list(map(int, list(input())))
N.sort(reverse=True)

# 리스트 언패킹, sep 으로 조건 맞춰서 결과 출력
print(*N, sep='')