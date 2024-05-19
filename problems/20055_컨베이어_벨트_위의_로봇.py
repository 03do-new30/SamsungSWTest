from collections import deque
n, k = map(int, input().split())
durability = deque(map(int, input().split())) # 내구도
robots = deque([False] * (n*2))

step = 1
while True:
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다
    durability.rotate(1)
    robots.rotate(1)
    # (n-1)번 칸에 있는 로봇을 없앤다
    if robots[n-1]:
        robots[n-1] = False
    
    # 2. 먼저 벨트에 올라간 로봇부터, 이동 가능하면 이동
    for i in range(2*n-1, -1, -1):
        if not robots[i]:
            continue
        next_i = i + 1
        if next_i == 2*n:
            next_i = 0
        if not robots[next_i] and durability[next_i] >= 1:
            durability[next_i] -= 1
            robots[next_i] = True
            robots[i] = False
        # (n-1)번 칸에 있는 로봇을 없앤다
        if robots[n-1]:
            robots[n-1] = False
    
    # 3. 올리는 위치에 로봇을 올린다
    if durability[0] > 0:
        durability[0] -= 1
        robots[0] = True

    # 4. 내구도가 0인 칸의 개수 검사
    cnt = 0
    for d in durability:
        if d == 0:
            cnt += 1
    if cnt >= k:
        break
    step += 1

print(step)