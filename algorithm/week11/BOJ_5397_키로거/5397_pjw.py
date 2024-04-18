T = int(input())  # 테스트 케이스 수
for _ in range(T):
    con_row = input()  # 명령어 문자열

    left_stack = []  # 커서 왼쪽 문자열을 저장하는 스택
    right_stack = []  # 커서 오른쪽 문자열을 저장하는 스택

    for char in con_row:
        if char == '<':
            if left_stack:
                right_stack.append(left_stack.pop())  # 커서를 왼쪽으로 이동시킴
        elif char == '>':
            if right_stack:
                left_stack.append(right_stack.pop())  # 커서를 오른쪽으로 이동시킴
        elif char == '-':
            if left_stack:
                left_stack.pop()  # 현재 커서 왼쪽에 있는 문자 삭제
        else:
            left_stack.append(char)  # 알파벳 추가

    # left_stack과 right_stack을 결합하여 결과 문자열을 생성
    result = ''.join(left_stack) + ''.join(reversed(right_stack))
    print(result)
