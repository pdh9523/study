# T : 테스트케이스 개수, S : 문자열
T = int(input())
S_lst = [list(input()) for _ in range(T)]

# recursion 함수 호출 횟수 변수 설정
cnt = 0

def recursion(s, l, r):
    global cnt   # 전역변수 설정
    cnt += 1     # recursion 함수 호출될 때마다 횟수 카운트업
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)

# cnt 가 전역변수이므로 첫 호출 이후로 cnt 가 누적되는 것을 방지하기 위해
# isPalindrome 함수가 호출 될때마다 cnt 초기화해준다.
def isPalindrome(s):
    global cnt   # 전역변수 설정
    cnt = 0      # isPalindrome 함수가 호출될 때마다 cnt 0으로 초기화
    return recursion(s, 0, len(s)-1)

for S in S_lst:
    print(isPalindrome(S), cnt)