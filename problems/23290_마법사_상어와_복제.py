from itertools import product

m, s = map(int, input().split())
arr = [[[] for _ in range(4)]for _ in range(4)]

for _ in range(m):
    r, c, d = map(int, input().split())
    r -= 1; c -=1; d -= 1
    arr[r][c].append(d)

shark_r, shark_c = map(int, input().split())
shark_r -= 1; shark_c -= 1

smell = [[0] * 4 for _ in range(4)]

# 물고기의 이동 방향
f_dr = [0, -1, -1, -1, 0, 1, 1, 1]
f_dc = [-1, -1, 0, 1, 1, 1, 0, -1]
arrows = {0:'←', 1:'↖', 2:'↑', 3:'↗', 4:'→', 5:'↘', 6:'↓', 7:'↙'}

# 상어의 이동 방향
dr = [0, -1, 0, 1, 0]
dc = [0, 0, -1, 0, 1]
# 연속해서 3칸 이동하는 방법을 만든다
orders = list(product([1, 2, 3, 4], repeat=3))

def print_arr_row(row):
    xx = []
    for tmp in row:
        result = []
        for x in tmp:
            result.append(arrows[x])
        xx.append(result)
    print(xx)

def get_copy_fish(arr):
    new_arr = [[[] for _ in range(4)] for __ in range(4)]
    for r in range(4):
        for c in range(4):
            for fish in arr[r][c]:
                if fish >= 0:
                    new_arr[r][c].append(fish)
    return new_arr

def turn_direction(i):
    if i == 0:
        return 7
    else:
        return i - 1
    
def in_range(r, c):
    return 0 <= r < 4 and 0 <= c < 4

def is_shark(r, c, shark_r, shark_c):
    return r == shark_r and c == shark_c

def is_smell(r, c):
    return smell[r][c] > 0

def fish_move(arr, smell, shark_r, shark_c):
    new_arr = [[[] for _ in range(4)] for __ in range(4)]
    for r in range(4):
        for c in range(4):
            if len(arr[r][c]) == 0:
                continue
            for fish in arr[r][c]:
                dir = fish
                nr = r + f_dr[dir]
                nc = c + f_dc[dir]
                first_nr = nr
                first_nc = nc
                movable = True
                while not in_range(nr, nc) or is_shark(nr, nc, shark_r, shark_c) or is_smell(nr, nc):
                    dir = turn_direction(dir)
                    nr = r + f_dr[dir]
                    nc = c + f_dc[dir]
                    if nr == first_nr and nc == first_nc:
                        movable = False
                        break
                
                if not movable:
                    new_arr[r][c].append(fish)
                    continue
                
                new_arr[nr][nc].append(dir)
    
    return new_arr

def shark_move(shark_r, shark_c):
    
    
    fish_cnt = dict()
    shark_loc = dict()
    history = dict()
    
    

    for order in orders:
        key = ''.join(map(str, order))
        key = int(key)
        
        r = shark_r
        c = shark_c
        impossible = False
        fishes = []
        tmp_cnt = 0
        for i in order:
            nr = r + dr[i]
            nc = c + dc[i]
            if not in_range(nr, nc):
                impossible = True
                break
            if len(arr[nr][nc]) > 0:
                # 물고기는 격자에서 제외되며 물고기 냄새를 남긴다
                if (nr, nc) not in fishes:
                    tmp_cnt += len(arr[nr][nc])
                    fishes.append((nr, nc))
            # update
            r = nr
            c = nc
        
        if impossible:
            continue
        
        history[key] = fishes
        shark_loc[key] = (nr, nc)
        fish_cnt[key] = tmp_cnt
    
    # 제외되는 물고기의 수가 가장 많은 방법을 찾는다 (사전순)
    sorted_keys = sorted(fish_cnt.keys())
    max_cnt = -1
    max_key = -1
    for key in sorted_keys:
        if max_cnt < fish_cnt[key]:
            max_cnt = fish_cnt[key]
            max_key = key
    # print("result", result)
    new_str = ''
    for x in str(max_key):
        x = int(x)
        if x == 1:
            new_str += '상'
        elif x == 2:
            new_str += '좌'
        elif x == 3:
            new_str += '하'
        else:
            new_str += '우'

    # print("상어 이동 >>>>", new_str)
    # print("max_key:", max_key)

    # print("history:", history)
    # print("fish_cnt:", fish_cnt)
    # print("shark_loc:", shark_loc)
    
    # max_key의 방법으로 이동한다
    new_shark_r, new_shark_c = shark_loc[max_key]
    
    # 결과를 보고 fish 없애준다
    for fish_r, fish_c in history[max_key]:
        # smell 업데이트
        smell[fish_r][fish_c] = 3
        # 사라질 물고기 arr에서 없애준다
        arr[fish_r][fish_c] = []
    

    # 상어의 위치 업데이트
    return new_shark_r, new_shark_c

def update_smell():
    for r in range(4):
        for c in range(4):
            if smell[r][c] == 0:
                continue
            if smell[r][c] - 1 <= 0:
                smell[r][c] = 0
            else:
                smell[r][c] -= 1

for _ in range(s):
    # print("@@@@@@@@@@", _ + 1, "turn: shark_r;", shark_r, "shark_c:", shark_c, "@@@@@@@@@@")
    # 1. 복제 마법
    copy_fish = get_copy_fish(arr)
    """
    print("### 복제마법")
    for row in copy_fish:
        print_arr_row(row)
    print('-' * 30)
    """
    # 2. 모든 물고기가 한 칸 이동한다
    arr = fish_move(arr, smell, shark_r, shark_c)
    """
    print("### 물고기 이동")
    for row in arr:
        print_arr_row(row)
    print('-' * 30)
    """

    # 상어가 연속해서 3칸 이동
    shark_r, shark_c = shark_move(shark_r, shark_c)
    """
    print("### 상어 이동 후 arr")
    for row in arr:
        print_arr_row(row)
    print('-' * 30)
    print("@@@ 상어 이동 후 smell")
    for row in smell:
        print(row)
    print('-' * 30)
    """
    # 두 번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라진다
    update_smell()
    """
    print("@@@ update 후 smell")
    for row in smell:
        print(row)
    print('-' * 30)
    """
    # 복제 마법이 완료된다
    for r in range(4):
        for c in range(4):
            if len(copy_fish[r][c]) == 0:
                continue
            for fish in copy_fish[r][c]:
                arr[r][c].append(fish)
    """
    print("### 복제 마법 완료")
    for row in arr:
        print_arr_row(row)
    print('-' * 30)
    """


# 남아있는 물고기의 수를 출력한다
answer = 0
for r in range(4):
    for c in range(4):
        answer += len(arr[r][c])
print(answer)