import sys
gomgom = set()                              # gomgom : 세트를 통해 중복 제거
t = int(input())
ans = 0                                     # ans : 인사한 곰곰이들

for _ in range(t):

    name = sys.stdin.readline().strip()     # name : 이름 입력 받고

    if name == "ENTER":                     # 그게 ENTER 면 
        ans += len(gomgom)                  # 안에 있는 곰곰이들 더하고
        gomgom = set()                      # 세트 다시 시작
        continue

    gomgom.add(name)                        # ENTER 이외에는 add 를 통해 계속 업데이트

ans += len(gomgom)                          # for 탈출 이후에 마지막으로 곰곰이들 더하기

print(ans)                                  # 출력