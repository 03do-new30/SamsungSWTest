from collections import namedtuple
n, m, sharks = map(int, input().split())
Shark = namedtuple("Shark", ["speed", "direction", "size"])
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, 1, -1]
arr = [[None] * (1 + m) for _ in range(n + 1)]
for _ in range(sharks):
    r, c, s, d, z = map(int, input().split())
    arr[r][c] = Shark(s, d, z)

answer = 0

def fish(c):
    global answer
    for r in range(1, n+1):
        if arr[r][c] is None:
            continue
        else:
            # 상어를 잡았다
            answer += arr[r][c].size
            arr[r][c] = None
            break

def counter_direction(i):
    if i == 1:
        return 2
    elif i == 2:
        return 1
    elif i == 3:
        return 4
    elif i == 4:
        return 3
    return 0

def shark_move():
    global arr
    shark_loc = []
    for r in range(1, n+1):
        for c in range(1, m+1):
            if arr[r][c] is not None:
                shark_loc.append((r, c))
    
    new_arr = [[None] * (m+1) for _ in range(n+1)]
    for r, c in shark_loc:
        count = arr[r][c].speed
        i = arr[r][c].direction
        size = arr[r][c].size
        
        nr = r; nc = c
        while count > 0:
            if 1 <= nr + dr[i] <= n and 1 <= nc + dc[i] <= m:
                nr += dr[i]
                nc += dc[i]
                count -= 1
            else:
                # 방향을 전환한다
                i = counter_direction(i)
        # 도착한 곳
        if new_arr[nr][nc] is None:
            new_arr[nr][nc] = Shark(arr[r][c].speed, i, size)
        else:
            if new_arr[nr][nc].size < size:
                new_arr[nr][nc] = Shark(arr[r][c].speed, i, size)
    # arr을 new_arr로 교체한다
    arr = new_arr


for c in range(1, m+1):
    fish(c)
    shark_move()
print(answer)