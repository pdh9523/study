import sys

T = int(sys.stdin.readline()) # 테케 수

for tc in range(1, T + 1):

    N = int(input()) # 지원자 수
    arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)] # 0번은 서류성적, 1번은 면접 성적
    # 지원자는 나머지 지원자 중 무작위 지원자보다 둘 다 성적이 떨어지면 탈락...
    # 아니면 붙음
    arr.sort()
    count = 0
    min_interview_score = float('inf')
    for i in range(N):
        if arr[i][1] < min_interview_score:
            count += 1
            min_interview_score = arr[i][1]
    
    print(count)