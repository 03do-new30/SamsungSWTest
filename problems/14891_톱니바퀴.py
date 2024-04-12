from collections import deque
gears = [[]]
for _ in range(4):
    gears.append(deque(map(int, input())))
k = int(input())
cmds = []
for _ in range(k):
    cmds.append(tuple(map(int, input().split())))

# gears[n][0] = 12시 방향
# gears[n][2] = 3시 방향
# gears[n][6] = 9시 방향
def rotate_gear(n, direction, visited):
    visited[n] = True
    # 옆에 있는 톱니바퀴와 서로 맞닿은 톱니의 극이 다르다면
    # 옆에 있는 톱니바퀴는 현재 톱니바퀴의 방향과 반대방향으로 회전한다
    # 왼쪽 방향 검사
    if 1 <= n-1:
        left = n-1
        if gears[left][2] != gears[n][6]:
            if not visited[left]:
                visited[left] = True
                rotate_gear(left, -direction, visited)
    # 오른쪽 방향 검사
    if n+1 <= 4:
        right = n+1
        if gears[n][2] != gears[right][6]:
            if not visited[right]:
                visited[right] = True
                rotate_gear(right, -direction, visited)
    # 회전
    gears[n].rotate(direction)
    

for n, direction in cmds:
    rotate_gear(n, direction, [False] * 5)
# 점수 계산
score = 0
for i in range(4):
    score += (2**i) * gears[i+1][0]
print(score)