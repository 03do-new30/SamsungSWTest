n = int(input())

blocks = {1:[(0, 0)], 2:[(0, 0), (0, 1)], 3:[(0, 0),(1, 0)]}

green_n = 6; green_m = 4
green = [[0] * 4 for _ in range(6)]
blue_n = 4; blue_m = 6
blue = [[0] * 6 for _ in range(4)]
score = 0 # 점수

def green_0_1(green):
    cnt = 0
    for i in range(2):
        for c in range(green_m):
            if green[i][c] != 0:
                cnt += 1
                break
    return cnt

def blue_0_1(blue):
    cnt = 0
    for i in range(2):
        for r in range(blue_n):
            if blue[r][i] != 0:
                cnt += 1
                break
    return cnt

def full_col(blue):
    for c in range(blue_m):
        zero_found = False
        for r in range(blue_n):
            if blue[r][c] == 0:
                zero_found = True
                break
        if not zero_found:
            return c # 꽉 찬 컬럼 번호를 반환
    return -1

def full_row(green):
    for r in range(green_n):
        zero_found = False
        for c in range(green_m):
            if green[r][c] == 0:
                zero_found = True
                break
        if not zero_found:
            return r # 꽉 찬 로우 번호를 반환
    return -1

def delete_row(green, target_row):
    for r in range(target_row -1, -1, -1):
        for c in range(green_m):
            green[r+1][c] = green[r][c]
    # 0번째 row를 전부 0으로 만든다
    for c in range(green_m):
        green[0][c] = 0

def delete_col(blue, target_col):
    for c in range(target_col-1, -1, -1):
        for r in range(blue_n):
            blue[r][c+1] = blue[r][c]
    # 0번째 col을 전부 0으로 만든다
    for r in range(blue_n):
        blue[r][0] = 0

def down_row(cnt):
    # cnt개만큼 row를 내려준다
    for r in range(green_n-cnt-1, -1, -1):
        for c in range(green_m):
            green[r + cnt][c] = green[r][c]
    # 위에서 cnt개만큼의 행을 비워준다
    for r in range(cnt):
        for c in range(green_m):
            green[r][c] = 0

def right_col(cnt):
    # cnt개만큼 col을 오른쪽으로 움직여준다
    for c in range(blue_m-cnt-1, -1, -1):
        for r in range(blue_n):
            blue[r][c + cnt] = blue[r][c]
    # 왼쪽에서 cnt개만큼의 행을 비워준다
    for c in range(cnt):
        for r in range(blue_n):
            blue[r][c] = 0


for turn in range(1, n+1):
    t, x, y = map(int, input().split())
    # print("turn:", turn, "t, x, y", t, x, y)
    dirs = blocks[t]
    # green
    # 블럭을 들어가게 한다
    gx = 0
    while gx +1 < green_n and green[gx+1][y] == 0:
        # 블럭 모양이 들어갈 수 있는지 확인한다
        fit = True
        for dr, dc in dirs:
            if 0 <= gx + 1 + dr < green_n and 0 <= y + dc < green_m:
                if green[gx+1+dr][y+dc] != 0:
                    fit = False
                    break
            else:
                fit = False
                break
        if not fit:
            break
        # gx update
        gx += 1
    
    
    for dr, dc in dirs:
        green[gx + dr][y + dc] = turn
    
    # 가득찬 행이 있는지 확인한다
    target_row = full_row(green)
    while target_row != -1:
        # 점수를 증가시킨다
        score += 1
        delete_row(green, target_row)
        target_row = full_row(green)
    
    # 연한 칸에 블록이 있는 경우 처리
    cnt = green_0_1(green)
    # cnt만큼 아래 행에 있는 타일이 사라진다
    down_row(cnt)
    
    # blue
    # 블럭을 들어가게 한다
    by = 0
    while by + 1 < blue_m and blue[x][by + 1] == 0:
        # 블럭 모양이 들어갈 수 있는지 확인한다
        fit = True
        for dr, dc in dirs:
            if 0 <= x + dr < blue_n and 0 <= by + 1 + dc < blue_m:
                if blue[x+dr][by+1+dc] != 0:
                    fit = False
                    break
            else:
                fit = False
                break
        if not fit:
            break
        # by update
        by += 1
    
    for dr, dc in dirs:
        blue[x + dr][by + dc] = turn
    
    # 가득찬 열이 있는지 확인한다
    target_col = full_col(blue)
    while target_col != -1:
        # 점수를 증가시킨다
        score += 1
        delete_col(blue, target_col)
        target_col = full_col(blue)
    
    # 연한 칸에 블록이 있는 경우 처리
    cnt = blue_0_1(blue)
    
    # cnt만큼 오른쪽에 있는 열이 사라진다
    right_col(cnt)

    # print("score:", score)
    # print("green")
    # for row in green:
    #     print(row)
    # print("blue")
    # for row in blue:
    #     print(row)
    # print('-' * 30)

green_blocks = 0
blue_blocks = 0
for r in range(green_n):
    for c in range(green_m):
        if green[r][c] != 0:
            green_blocks += 1
for r in range(blue_n):
    for c in range(blue_m):
        if blue[r][c] != 0:
            blue_blocks += 1

print(score)
print(green_blocks + blue_blocks)

"""
10
2 3 2
3 1 3
3 1 1
3 1 2
1 1 0
2 0 0
2 0 2
2 0 2
2 0 2
1 0 0
"""