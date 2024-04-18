for _ in range(int(input())):
    testcase = input()
    left_stack = []
    right_stack = []

    for x in testcase:
        if x.isalnum():
            left_stack.append(x)
        elif x == '-':
            if left_stack:
                left_stack.pop()
        elif x == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        else:
            if right_stack:
                left_stack.append(right_stack.pop())

    result = ''.join(left_stack + right_stack[::-1])
    print(result)



'시간초과 25%'

# for _ in range(int(input())):
#     testcase = input()
#     stack = []
#     cursor = 0
#
#     for i in range(len(testcase)):
#         if testcase[i].isalnum():
#             stack.insert(cursor, testcase[i])
#             cursor += 1
#         elif testcase[i] == '-' and cursor > 0:
#             cursor -= 1
#             stack.pop(cursor)
#         elif testcase[i] == '<' and cursor > 0:
#             cursor -= 1
#         elif testcase[i] == '>' and cursor < len(stack):
#             cursor += 1
#
#     print(''.join(stack))