N, M = map(int, input().split()) # 입력 걸그룹, 맞힐 문제

groups = {}
for tc in range(N):
    g_name = input()
    member_num = int(input())
    members = [input() for _ in range(member_num)]
    groups[g_name] = members # 딕셔너리에 넣자.

quiz = [input() for _ in range(2*M)]

for i in range(1, 2*M, 2): # 숫자
    if quiz[i] == '0':
        alpha = groups[quiz[i-1]]
        alpha.sort()
        for member in alpha:
            print(member)
    else:
        target = quiz[i-1]
        for key, value in groups.items():
            if target in value:
                print(key)
                break
