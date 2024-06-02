from collections import deque
from math import floor

n, m, k = map(int, input().split())
arr = [[0] * (m+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

# wall[x][y][0]이 True이면 (x,y)와 (x-1,y) 사이에 벽
# wall[x][y][1]이 True이면 (x,y)와 (x,y+1) 사이에 벽
wall = [[[False] * 2 for __ in range(m+1)] for _ in range(n+1)]
w = int(input())
for _ in range(w):
    r, c, flag = map(int, input().split())
    wall[r][c][flag] = True

# 바람의 방향
dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]
# 방의 온도
temperatures = [[0] * (m+1) for _ in range(n+1)]

def in_range(r, c):
    return 1 <= r <= n and 1 <= c <= m

def rotate_90(board):
    n = len(board)
    m = len(board[0])
    new_board = [[0] * n for _ in range(m)]
    for r in range(n):
        for c in range(m):
            new_board[c][n-1-r] = board[r][c]
    return new_board

def rotate_180(board):
    n = len(board)
    m = len(board[0])
    new_board = [[0] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            new_board[n-1-r][m-1-c] = board[r][c]
    return new_board

def rotate_270(board):
    n = len(board)
    m = len(board[0])
    new_board = [[0] * n for _ in range(m)]
    for r in range(n):
        for c in range(m):
            new_board[m-1-c][r] = board[r][c]
    return new_board

def get_wind_temp(dir):
    wind_temp = [
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 2, 1],
        [0, 0, 0, 3, 2, 1],
        [0, 0, 4, 3, 2, 1],
        [-1, 5, 4, 3, 2, 1],
        [0, 0, 4, 3, 2, 1],
        [0, 0, 0, 3, 2, 1],
        [0, 0, 0, 0, 2, 1],
        [0, 0, 0, 0, 0, 1]
    ]
    if dir == 1: # 오른쪽
        return wind_temp
    elif dir == 2: # 왼쪽
        return rotate_180(wind_temp)
    elif dir == 3: # 위
        return rotate_270(wind_temp)
    else: # 아래
        return rotate_90(wind_temp)

def is_wall(r, c, dr, dc):
    # 벽 검사
    # wall[x][y][0]이 True이면 (x,y)와 (x-1,y) 사이에 벽
    # wall[x][y][1]이 True이면 (x,y)와 (x,y+1) 사이에 벽
    if dr != 0:
        if dr == 1: # 아래
            if in_range(r+1, c) and wall[r+1][c][0]:
                return True
        else: # 위
            if wall[r][c][0]:
                return True
    if dc != 0:
        if dc == 1: # 오른쪽
            if wall[r][c][1]:
                return True
        else: # 왼쪽
            if in_range(r, c-1) and wall[r][c-1][1]:
                return True
    return False

def spread_wind(r, c, dir, value, visited):
    if value == 0:
        return
    # value == 5인 경우 값을 기록한다
    if value == 5:
        visited[r][c] = value
    # 오른쪽이나 왼쪽인 경우
    if dir == 1 or dir == 2:
        # 정방향
        nr = r + dr[dir]
        nc = c + dc[dir]
        if in_range(nr, nc) and visited[nr][nc] == 0:
            has_wall = is_wall(r, c, dr[dir], dc[dir])
            if not has_wall:
                visited[nr][nc] = value - 1
                spread_wind(nr, nc, dir, value -1, visited)
            else:
                visited[nr][nc] = -1
        # 대각선 위
        upper_nr = nr - 1
        if in_range(upper_nr, nc) and visited[upper_nr][nc] == 0:
            has_wall = is_wall(r, c, -1, dc[dir])
            if not has_wall:
                visited[upper_nr][nc] = value - 1
                spread_wind(upper_nr, nc, dir, value - 1, visited)
            else:
                visited[upper_nr][nc] = -1
        # 대각선 아래
        lower_nr = nr + 1
        if in_range(lower_nr, nc) and visited[lower_nr][nc] == 0:
            has_wall = is_wall(r, c, 1, dc[dir])
            if not has_wall:
                visited[lower_nr][nc] = value - 1
                spread_wind(lower_nr, nc, dir, value - 1, visited)
            else:
                visited[lower_nr][nc] = -1
    # 위쪽이나 아래쪽인 경우
    else:
        # 정방향
        nr = r + dr[dir]
        nc = c + dc[dir]
        if in_range(nr, nc) and visited[nr][nc] == 0:
            has_wall = is_wall(r, c, dr[dir], dc[dir])
            print("r:", r, "c:", c, "nr:", nc, "nc:", nc, "haswall:", has_wall)
            if not has_wall:
                visited[nr][nc] = value - 1
                spread_wind(nr, nc, dir, value -1, visited)
            else:
                visited[nr][nc] = -1
        # 대각선 왼쪽
        left_nc = nc - 1
        if in_range(nr, left_nc) and visited[nr][left_nc] == 0:
            has_wall = is_wall(r, c, dr[dir], -1)
            if not has_wall:
                visited[nr][left_nc] = value - 1
                spread_wind(nr, left_nc, dir, value - 1, visited)
            else:
                visited[nr][left_nc] = -1
        # 대각선 오른쪽
        right_nc = nc + 1
        if in_range(nr, right_nc) and visited[nr][right_nc] == 0:
            has_wall = is_wall(r, c, dr[dir], 1)
            if not has_wall:
                visited[nr][right_nc] = value - 1
                spread_wind(nr, right_nc, dir, value - 1, visited)
            else:
                visited[nr][right_nc] = -1

def wind():
    for r in range(1, n+1):
        for c in range(1, m+1):
            if arr[r][c] == 0 or arr[r][c] == 5:
                continue
            visited = [[0] * (m+1) for _ in range(n+1)]
            spread_wind(r, c, arr[r][c], 5, visited)
            print("visited")
            for row in visited:
                print(row)
            for x in range(1, n+1):
                for y in range(1, m+1):
                    temperatures[x][y] += visited[x][y]

            """wind_temp = get_wind_temp(arr[r][c])
            # for row in wind_temp:
            #     print(row)
            # print('~' * 30)
            # wind_temp에 기록된 온풍기의 시작점
            tmp_r = 0; tmp_c = 0
            for x in range(len(wind_temp)):
                for y in range(len(wind_temp[0])):
                    if wind_temp[x][y] == -1:
                        tmp_r = x
                        tmp_c = y
                        break
            # tmp_r, tmp_c를 기준으로 온도를 기록해간다
            for x in range(len(wind_temp)):
                for y in range(len(wind_temp[0])):
                    if wind_temp[x][y] > 0:
                        # tmp_r과의 차이
                        r_diff = x - tmp_r
                        c_diff = y - tmp_c
                        # 실제 (r, c)에 적용하는 경우
                        nr = r + r_diff
                        nc = c + c_diff
                        if not in_range(nr, nc):
                            continue
                        # 벽 검사
                        # wall[x][y][0]이 True이면 (x,y)와 (x-1,y) 사이에 벽
                        # wall[x][y][1]이 True이면 (x,y)와 (x,y+1) 사이에 벽
                        print("r_diff:", r_diff, "c_diff:", c_diff)
                        if r_diff != 0:
                            if r_diff == -1:
                                if wall[r][c][0]:
                                    continue
                            elif r_diff == 1:
                                if wall[r+1][c][0]:
                                    continue
                        if c_diff != 0:
                            if c_diff == -1:
                                if wall[r][c-1][1]:
                                    continue
                            elif c_diff == 1:
                                if wall[r][c][1]:
                                    continue
                        add_tmps[nr][nc] += wind_temp[x][y]
            print("add tmps at r:", r, "c:", c)
            for rr in range(1, n+1):
                print(add_tmps[rr][1:])
    # add_tmps
    for r in range(n):
        for c in range(n):
            temperatures[r][c] += add_tmps[r][c]"""

def adjust_temperatures(r, c, visited, new_temperatures):
    q = deque([(r, c)])
    visited[r][c] = True
    while q:
        r, c = q.popleft()
        current = temperatures[r][c]

        for i in range(1, 5):
            nr = r + dr[i]
            nc = c + dc[i]
            if in_range(nr, nc) and not visited[nr][nc]:
                if current <= temperatures[nr][nc]:
                    continue
                # 두 칸 사이에 벽이 있는지 확인한다
                # wall[x][y][0]이 True이면 (x,y)와 (x-1,y) 사이에 벽
                # wall[x][y][1]이 True이면 (x,y)와 (x,y+1) 사이에 벽
                if dr[i] != 0:
                    if dr[i] == -1:
                        if wall[r][c][0]:
                            continue
                    elif dr[i] == 1:
                        if wall[r+1][c][0]:
                            continue
                if dc[i] != 0:
                    if dc[i] == -1:
                        if wall[r][c-1][1]:
                            continue
                    elif dc[i] == 1:
                        if wall[r][c][1]:
                            continue
                next_temperature = floor((current - temperatures[nr][nc]) / 4)
                # 낮은 칸은 온도 상승
                new_temperatures[nr][nc] += next_temperature
                # 높은 칸은 온도 감소
                new_temperatures[r][c] -= next_temperature

                # 만약 temperatrues[nr][nc]에 온도가 있었다면 visited 배열에 추가해주고 큐에 추가해준다
                if temperatures[nr][nc] > 0:
                    visited[nr][nc] = True
                    q.append((nr, nc))

def check():
    # 조사하는 모든 칸의 온도가 K 이상이 되었는지 검사한다
    for r in range(1, n+1):
        for c in range(1, n+1):
            if arr[r][c] == 5:
                if temperatures[r][c] < k:
                    return False
    return True

chocolate = 0
turn = 1
while not check():
    if turn == 3:
        break
    print("####### turn:", turn , "#######")
    # 집에 있는 모든 온풍기에서 바람이 한 번 나옴
    wind()
    print("[!] 바람이 나온 뒤 온도의 상태")
    for r in range(1, n+1):
        print(temperatures[r][1:])
    print('-' * 30)
    # 온도가 조절됨
    visited = [[False] * (m+1) for _ in range(n+1)]
    new_temperatures = [[0] * (m+1) for _ in range(n+1)]
    for r in range(1, n+1):
        for c in range(1, m+1):
            if not visited[r][c]:
                adjust_temperatures(r, c, visited, new_temperatures)
    for r in range(1, n+1):
        for c in range(1, m+1):
            temperatures[r][c] += new_temperatures[r][c]

    # 온도가 1 이상인 가장 바깥쪽칸의 온도가 1씩 감소
    for r in range(1, n+1):
        for c in range(1, n+1):
            if r == 1 or r == n or c == 1 or c == n:
                if temperatures[r][c] >= 1:
                    temperatures[r][c] -= 1

    # 초콜릿을 먹음
    chocolate += 1

    for r in range(1, n+1):
        print(temperatures[r][1:])
    print('-' * 30)
    turn += 1

print("chocolate:", chocolate)

# visited = [[0] * (m+1) for _ in range(n+1)]
# spread_wind(2, 5, 4, 5, visited)
# for row in visited:
#     print(row)