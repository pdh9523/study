N,M = map(int,input().split())

S,T = input(),input()
sdx, tdx = [],[]
# 각각 문자열에서 n번째 1의 인덱스를 저장
for i in range(len(S)):
    if S[i] == "1":
        sdx.append(i)

for j in range(len(T)):
    if T[j] == "1":
        tdx.append(j)
# 차이들을 조합하고, 총 움직이는 수를 구함
tmp = 0
for idx in range(M):
    tmp += abs(sdx[idx] - tdx[idx])
# 최소값은 항상 반반 움직였을 때
ans = (tmp//2)**2 + (tmp-tmp//2)**2
print(ans)