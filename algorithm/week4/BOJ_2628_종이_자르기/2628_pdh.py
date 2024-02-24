N,M = map(int,input().split())
 
t = int(input())

n_list = [0,N]      # 잘린 종이 인덱스
m_list = [0,M]

sorted_m = []       # 자른 크기 담아둘 인덱스
sorted_n = []


for _ in range(t):
    way, point = map(int,input().split())
    
    if way == 0 :
        m_list.append(point)
    else :
        n_list.append(point)

m_list.sort()
n_list.sort()

for i in range(len(m_list)-1) :                 
    sorted_m.append(m_list[i+1]-m_list[i])      # 큰거에서 작은걸 빼면 크기가 담긴다

for j in range(len(n_list)-1) :
    sorted_n.append(n_list[j+1]-n_list[j])

print(max(sorted_m) * max(sorted_n))            # 그 중 가장 큰거 두개를 곱해라