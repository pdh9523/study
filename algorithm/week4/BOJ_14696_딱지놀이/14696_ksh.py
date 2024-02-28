N = int(input())   # 딱지놀이의 총 라운드 수
for i in range(N):
    A = list(map(int, input().split()))   # A 의 딱지 정보
    B = list(map(int, input().split()))   # B 의 딱지 정보

    a = A.pop(0)
    b = B.pop(0)

    if A.count(4) > B.count(4):   # 별의 개수 비교
        print('A')
    elif A.count(4) < B.count(4):
        print('B')
    else:                         # 별의 개수가 같다면
        if A.count(3) > B.count(3):   # 동그라미의 개수 비교
            print('A')
        elif A.count(3) < B.count(3):
            print('B')
        else:                         # 동그라미의 개수가 같다면
            if A.count(2) > B.count(2):    # 네모의 개수 비교
                print('A')
            elif A.count(2) < B.count(2):
                print('B')
            else:                          # 네모의 개수가 같다면
                if A.count(1) > B.count(1):    # 세모의 개수 비교
                    print('A')
                elif A.count(1) < B.count(1):
                    print('B')
                else:                          # 세모의 개수가 같다면 무승부
                    print('D')