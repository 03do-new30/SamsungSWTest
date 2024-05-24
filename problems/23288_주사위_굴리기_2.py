from collections import deque

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
dice = {"top":1, "left":4, "right":3, "front":5, "back":2, "bottom":6}

# 가장 처음 이동 방향
idx = 0 # 동쪽

# 점수
score = 0

# 현재 이동 방향의 반대 방향
def get_opposite_idx(idx):
    if idx == 0:
        return 1
    elif idx == 1:
        return 0
    elif idx == 2:
        return 3
    else:
        return 2

# 현재 이동 방향의 90도 시계방향
def get_90_idx(idx):
    if idx == 0: # 동
        return 3
    elif idx == 1: # 서
        return 2
    elif idx == 2: # 북
        return 0
    elif idx == 3: # 남
        return 1

# 현대 이동 방향의 90도 반시계방향
def get_270_idx(idx):
    if idx == 0: # 동
        return 2
    elif idx == 1: # 서
        return 3
    elif idx == 2: # 북
        return 1
    else : # 남
        return 0

# 범위 검사
def in_range(r, c):
    return 0 <= r < n and 0 <= c < m

# 동쪽으로 굴린다
def east():
    global dice
    new_dice = dict()
    new_dice["top"] = dice["left"]
    new_dice["left"] = dice["bottom"]
    new_dice["right"] = dice["top"]
    new_dice["front"] = dice["front"]
    new_dice["back"] = dice["back"]
    new_dice["bottom"] = dice["right"]
    dice = new_dice

# 서쪽으로 굴린다
def west():
    global dice
    new_dice = dict()
    new_dice["top"] = dice["right"]
    new_dice["left"] = dice["top"]
    new_dice["right"] = dice["bottom"]
    new_dice["front"] = dice["front"]
    new_dice["back"] = dice["back"]
    new_dice["bottom"] = dice["left"]
    dice = new_dice

# 북쪽으로 굴린다
def north():
    global dice
    new_dice = dict()
    new_dice["top"] = dice["front"]
    new_dice["left"] = dice["left"]
    new_dice["right"] = dice["right"]
    new_dice["front"] = dice["bottom"]
    new_dice["back"] = dice["top"]
    new_dice["bottom"] = dice["back"]
    dice = new_dice

# 남쪽으로 굴린다
def south():
    global dice
    new_dice = dict()
    new_dice["top"] = dice["back"]
    new_dice["left"] = dice["left"]
    new_dice["right"] = dice["right"]
    new_dice["front"] = dice["top"]
    new_dice["back"] = dice["bottom"]
    new_dice["bottom"] = dice["front"]
    dice = new_dice

# 주사위가 도착한 칸 (r, c)에 대한 점수 획득
def get_score(r, c):
    target = arr[r][c]
    q = deque([(r, c)])
    visited = [[False] * m for _ in range(n)]
    visited[r][c] = True
    # 칸 수
    cnt = 0
    while q:
        r, c = q.popleft()
        cnt += 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if in_range(nr, nc):
                if arr[nr][nc] == target:
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr, nc))
    return cnt * target
                    

# 주사위의 이동
def move(r, c):
    global idx
    # 1. 
    nr = r + dr[idx]
    nc = c + dc[idx]
    # 이동 방향에 칸이 없다면 이동 방향을 반대로 한 다음 한 칸 굴러감
    if not in_range(nr, nc):
        idx = get_opposite_idx(idx)
        nr = r + dr[idx]
        nc = c + dc[idx]
    # 이동방향으로 주사위를 굴려준다
    if idx == 0: # 동
        east()
    elif idx == 1: # 서
        west()
    elif idx == 2: # 북
        north()
    else: # 남
        south()
    
    # 2. 주사위가 도착한 칸에 대한 점수를 획득한다
    global score
    score += get_score(nr, nc)

    # 3. 이동 방향을 결정한다
    bot_num = dice["bottom"]
    if bot_num > arr[nr][nc]:
        idx = get_90_idx(idx)
    elif bot_num < arr[nr][nc]:
        idx = get_270_idx(idx)
    
    return nr, nc # 현재 위치를 리턴한다

r = 0; c = 0
for _ in range(k):
    next_r, next_c = move(r, c)
    r = next_r
    c = next_c
print(score)
