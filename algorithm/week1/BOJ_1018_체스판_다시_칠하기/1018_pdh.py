bw = "BWBWBWBW"
wb = "WBWBWBWB"
bw_list = ([bw] + [wb]) * 4
# 유사도를 어떻게 판별할 것인가?
output_list = [] # 리스트 만들기
x, y = map(int,input().split()) # 제시된 숫자
test_list = [input() for _ in range(x)] # 제시된 체스판
for i in range(x-7) : # 체스판 자를 때 기준은 x - 8 + 1
    for j in range(y-7) : 
        bw_output = 0 # output 담을 변수 설정
        for idx in range(8) :
            for jdx in range(8) :
                if bw_list[idx][jdx] == test_list[i+idx][j+jdx] : # 같으면
                    bw_output += 1 # +1
        output_list.append(bw_output)
output_list += list(map(lambda x : 64-x, output_list)) # 64에서 도출된 값을 빼면 반대 무늬 체스판의 결과가 나옴

print(min(output_list)) # 거기서 최소치를 구함