from collections import deque

N, K = map(int, input().split())   # 컨베이어 벨트 길이 N, 벨트 길이 2*N, 내구도 0 허용 칸 수 K
durability = deque(map(int, input().split()))

belt_robot = deque([0] * 2 * N)    # 벨

level = 0   # 단계
# 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
while durability.count(0) < K:
    level += 1
    # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    belt_robot.appendleft(belt_robot.pop())
    durability.appendleft(durability.pop())

    if belt_robot[N - 1] == 1:
        belt_robot[N - 1] = 0

    # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
        # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
        # => 현재 칸(i) 기준으로 다음 칸(i + 1)에 로봇이 있는지 확인
        # => 현재 칸(i) 기준으로 다음 칸(i + 1)에 내구도 1 이상인지 확인
    for i in range(N - 2, -1, -1):
        if belt_robot[i] == 1 and belt_robot[i + 1] == 0 and durability[i + 1] != 0:
            belt_robot[i], belt_robot[i + 1] = 0, 1
            durability[i + 1] -= 1

    if belt_robot[N - 1] == 1:
        belt_robot[N - 1] = 0

    # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    # => 올리는 위치(i == 0)의 내구도 1 이상일 때 로봇을 올린다.
    if durability[0] != 0:
        belt_robot[0] = 1
        durability[0] -= 1

print(level)