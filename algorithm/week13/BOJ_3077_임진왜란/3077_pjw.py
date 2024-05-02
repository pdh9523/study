N = int(input()) # 해전 개수
submit = input().split()
answer = input().split()

# 이거 맨 앞 부터 비교해서 다르면 N(N-1)/2 에서 N-1부터 빼나가면 됨.
# 뺐으면 pop 한다, a가 0이되거나 submit이 비었으면 종료하고 a/b 출력
# pop하니까 for문 못돌림... 걍 돌려봄
answer_dict = {word: idx for idx, word in enumerate(submit)}

# print(answer_dict)
count = 0

for i in range(N):
    for j in range(i+1, N):
        if answer_dict[answer[i]] < answer_dict[answer[j]]:
            count +=1
result = N * (N-1)//2

print(f'{count}/{result}')

