'딕셔너리, 리스트 컴프리헨션 활용'

N, M = map(int, input().split())   # 걸그룹의 수 N, 문제의 수 M
idol = {}
for _ in range(N):
    team = input()
    member_num = int(input())
    idol[team] = [input() for _ in range(member_num)]
for _ in range(M):
    quiz_content = input()
    quiz = int(input())
    if quiz == 0:
        answer = idol.get(quiz_content)
        answer.sort()
        for i in range(len(answer)):
            print(answer[i])
    else:
        answer = [k for k, v in idol.items() if quiz_content in v]
        print(*answer)