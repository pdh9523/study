count = 0 # 문제에 있는 코드 복붙하고
def recursion(s, l, r):
    global count # 카운트 글로벌로 받아서 재귀 돌아갈때마다 올렸습니다.
    count += 1
    if l >= r: 
        return 1
    elif s[l] != s[r]: 
        return 0
    else: 
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

t = int(input())

for _ in range(t) :
    test_case = input()
    print(isPalindrome(test_case), count) # 수고..
    count = 0 # for문 돌때마다 카운트 초기화 한번씩