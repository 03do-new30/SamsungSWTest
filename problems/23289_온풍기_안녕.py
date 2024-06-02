from math import floor
from collections import deque

n, m, k = map(int, input().split())
# 방의 정보
arr =[[0] * (m+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
# 벽
w = int(input())
# 위쪽에 벽이 있음
upper_wall = [[False] * (m+1) for _ in range(n+1)]
# 오른쪽에 벽이 있음
right_wall = [[False] * (m+1) for _ in range(n+1)]
    
for _ in range(w):
    r, c, type = map(int, input().split())
    if type == 0:
        upper_wall[r][c] = True
    else:
        right_wall[r][c] = True

# 방의 온도
temperatures = [[0] * (m+1) for _ in range(n+1)]

def in_range(r, c):
    return 1 <= r <= n and 1 <= c <= m

# (r, c)가 (r + dr, c + dc)로 이동할 때, 이동을 막는 벽이 있는지
def has_wall(r, c, dr, dc):
    if dr != 0:
        if dr == -1: # 위쪽
            if upper_wall[r][c]:
                return True
        elif dr == 1: # 아래쪽
            if in_range(r + dr, c) and upper_wall[r + dr][c]:
                return True
    
    if dc != 0:
        if dc == -1: # 왼쪽
            if in_range(r, c + dc) and right_wall[r][c+dc]:
                return True
            pass
        elif dc == 1: # 오른쪽
            if right_wall[r][c]:
                return True
    
    return False

def corner_has_wall(r, c, major_dr, major_dc, minor_dr, minor_dc):
    # major 바람 방향이 오른쪽이나 왼쪽일 경우
    # minor 바람 방향은 위/아래
    
    # major 바람 방향이 위/아래인 경우
    # minor 바람 방향은 오/왼
    
    # minor 방향으로 움직일 수 있는지 검사한다
    minor_wall = has_wall(r, c, minor_dr, minor_dc)
    if minor_wall:
        return True
    else:
        nr = r + minor_dr
        nc = c + minor_dc
        # major 방향으로 움직일 수 있는지 검사한다
        major_wall = has_wall(nr, nc, major_dr, major_dc)
        if major_wall:
            return True
    return False


# 1. 집에 있는 모든 온풍기에서 바람이 한 번 나옴
def next_locs(r, c, dr, dc):
    locs = []
    # 정방향
    nr = r + dr
    nc = c + dc
    if in_range(nr, nc):
        locs.append((nr, nc))
    # 오른쪽이나 왼쪽이면 위, 아래로
    if dr == 0:
        if in_range(nr-1, nc):
            locs.append((nr - 1, nc))
        if in_range(nr+1, nc):
            locs.append((nr + 1, nc))
    # 위쪽이나 아래쪽이면 오, 왼으로
    else:
        if in_range(nr, nc-1):
            locs.append((nr, nc-1))
        if in_range(nr, nc+1):
            locs.append((nr, nc+1))

    return locs

def blow_wind(wind_temp, r, c, i):
    original_r = r; original_c = c
    # 1:오, 2:왼, 3:위, 4:아래
    dr = [0, 0, 0, -1, 1]
    dc = [0, 1, -1, 0, 0]
    tmp = [[0] * (m+1) for _ in range(n+1)]
    # 처음으로 바람이 퍼지는 위치
    start_r = r + dr[i]
    start_c = c + dc[i]
    if in_range(start_r, start_c) and not has_wall(r, c, dr[i], dc[i]):
        q = deque([(start_r, start_c, 5)])
        tmp[start_r][start_c] = 5
    else:
        return
    
    while q:
        r, c, cnt = q.popleft()
        if cnt == 1:
            continue
        # 다음으로 바람이 퍼질 세 곳
        locs = next_locs(r, c, dr[i], dc[i])
        for nr, nc in locs:
            if nr-r == dr[i] and nc-c == dc[i]: # 정방향
                if has_wall(r, c, nr-r, nc-c):
                    continue
            else: # 대각선
                if corner_has_wall(r, c, dr[i], dc[i], nr-r-dr[i], nc-c-dc[i]):
                    continue
            if tmp[nr][nc] == 0:
                tmp[nr][nc] = cnt - 1
                q.append((nr, nc, cnt -1))
        
    
    # wind_temp에 tmp 값을 합쳐준다
    for r in range(1, n+1):
        for c in range(1, m+1):
            wind_temp[r][c] += tmp[r][c]
    
    # print("r:", original_r, "c:", original_c, "에서 나오는 온풍기 바람")
    # for row in tmp:
    #     print(row)
    # print('=' * 30)
        

def wind():
    for r in range(1, n+1):
        for c in range(1, m+1):
            if arr[r][c] == 0 or arr[r][c] == 5:
                continue
            blow_wind(wind_temp, r, c, arr[r][c])

def add_wind(wind_temp):
    # 온풍기에서 나오는 바람의 온도를 temperature에 합쳐줌
    for r in range(1, n+1):
        for c in range(1, m+1):
            temperatures[r][c] += wind_temp[r][c]



# 2. 온도 조절
def adjust():
    # 모든 인접한 칸에 대해서 온도가 높은 칸 -> 낮은 칸으로 온도가 조절
    # 조절되는 온도
    memos = [[0] * (m+1) for _ in range(n+1)]
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    for r in range(1, n+1):
        for c in range(1, m+1):
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not in_range(nr, nc):
                    continue
                if has_wall(r, c, dr[i], dc[i]):
                    continue
                value = floor(abs(temperatures[r][c] - temperatures[nr][nc]) / 4)
                if temperatures[r][c] > temperatures[nr][nc]:
                    memos[r][c] -= value
                elif temperatures[r][c] < temperatures[nr][nc]:
                    memos[r][c] += value
    
    # memos의 값을 temperatures에 합쳐주어 온도 조절
    for r in range(1, n+1):
        for c in range(1, m+1):
            temperatures[r][c] += memos[r][c]

# 3. 온도가 1 이상인 가장 바깥쪽 칸의 온도를 1씩 감소시킨다
def corner_down():
    for r in range(1, n+1):
        for c in range(1, m+1):
            if r == 1 or r == n or c == 1 or c == m:
                if temperatures[r][c] >= 1:
                    temperatures[r][c] -= 1

# 5. 조사하는 모든 칸의 온도가 K 이상인지 검사
def is_done():
    for r in range(1, n+1):
        for c in range(1, m+1):
            if arr[r][c] == 5:
                if temperatures[r][c] >= k:
                    continue
                else:
                    return False
    return True

def print_temp():
    for row in temperatures:
        print(row)
    print('-' * 30)

chocolate = 0

wind_temp = [[0] * (m+1) for _ in range(n+1)]
wind() # wind_temp 구성

while True:
    # print("########## chocolate:", chocolate, "#" * 10)
    if chocolate == 100:
        chocolate = 101
        break
    add_wind(wind_temp)

    # print("=== after 온풍기 작동 ===")
    # print_temp()

    adjust()
    # print("=== after 온도조정 ===")
    # print_temp()

    corner_down()
    # print('=== after 모서리 온도 다운 ===')
    # print_temp()

    chocolate += 1
    
    if is_done():
        break
print(chocolate)