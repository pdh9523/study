D, K = map(int, input().split()) # 날 3~30, 떡 10~10만 => 어케 떡을 10만개 들고다니냐?

# d = 6 , k = 41 로 가정하자

def numbers(D, K):
    for a in range(1, K):
        for b in range(1, K):
            count = 2
            num1, num2 = a, b
            while True:
                next_num = num1 + num2
                # print(num1, num2)
                if next_num == K:
                    if count == D-1:
                        return a, b
                    else:
                        break
                num1, num2 = num2, next_num
                count += 1
                if count > D-1:
                    break
            


result = numbers(D, K)
print(result[0])
print(result[1])
