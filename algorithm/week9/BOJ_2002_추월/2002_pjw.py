N = int(input())  # 차량 대수
arr1 = [input() for _ in range(N)]  # 대근이, 입구
arr2 = [input() for _ in range(N)]  # 영식이, 출구

# 차량 번호 인덱스 딕셔너리 생성
in_index = {car: idx for idx, car in enumerate(arr1)}


cnt = 0


for i in range(N):
    # 추월이 발생하는지 확인
    for j in range(i + 1, N):
        in_car_i, in_car_j = arr1[i], arr1[j]
        out_car_i, out_car_j = arr2[i], arr2[j]
        # 대근이의 입구 차량 순서가 영식이의 출구 차량 순서 이전에 등장하면 추월이 발생
        if in_index[in_car_i] < in_index[in_car_j] and in_index[out_car_i] > in_index[out_car_j]:
            cnt += 1
            break  # 추월이 발생했으므로 더 이상 확인할 필요가 없음

print(cnt)



