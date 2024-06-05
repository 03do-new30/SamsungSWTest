bowls, k = map(int, input().split())
arr = []
for x in map(int, input().split()):
    arr.append([x])

def print_it(arr):
    n = len(arr)
    m = len(arr[0])
    tmp = [[0] * m for _ in range(n)]
    for i in range(n):
        if len(arr[i]) == 0:
            break
        for j in range(len(arr[i])):
            tmp[i][j] = arr[i][j]
    # tmp를 왼쪽으로 90도 회전해준다
    new_tmp = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_tmp[m-1-j][i] = tmp[i][j]
    for row in new_tmp:
        print(row)
    print('-' * 30)

def add_fish():
    global arr

    min_fish = float('inf')
    min_locs = []
    n = len(arr)
    for i in range(n):
        for j in range(len(arr[i])):
            if min_fish > arr[i][j]:
                min_fish = arr[i][j]
                min_locs = [(i, j)]
            elif min_fish == arr[i][j]:
                min_locs.append((i, j))
    # +1
    for i, j in min_locs:
        arr[i][j] += 1

def stack_bowl():
    global arr

    if len(arr) <= 1:
        return
    leftmost = arr[0]
    new_arr = arr[1:]
    for x in leftmost:
        new_arr[0].append(x)
    
    arr = new_arr

def has_floor(floated, new_arr):
    # 90도 회전시키기 전 floated와 new_arr를 비교하면
    # 중단할지 계속할지 판단할 수 있음
    return len(floated[0]) <= len(new_arr)

def rotate_90(floated):
    n = len(floated)
    m = len(floated[0])
    new_floated = [[0] * n for _ in range(m)]
    for r in range(n):
        for c in range(m):
            new_floated[c][n-1-r] = floated[r][c]
    return new_floated

def float_and_rotate(arr):
    n = len(arr)
    # 2개 이상 쌓여있는 어항
    floated = []
    floated_idx = 0
    for i in range(n):
        if len(arr[i]) >= 2:
            floated.append(arr[i])
            floated_idx = i
        else:
            break
    if len(floated) == 0:
        return arr
    # 2개 이상 쌓인 어항을 제외한 나머지
    if floated_idx + 1 < n:
        new_arr = arr[floated_idx + 1:]
        if has_floor(floated, new_arr):
            # floated를 90도 회전하고 new_arr에 붙인다
            new_floated = rotate_90(floated)
            # print("*****")
            # print("new_floated")
            # print(new_floated)
            # print("new_arr")
            # print(new_arr)
            for r in range(len(new_floated)):
                for fish in new_floated[r]:
                    new_arr[r].append(fish)
            # 다음 턴을 계속한다
            return float_and_rotate(new_arr)
    return arr

def adjust_fish():
    n = len(arr)
    m = len(arr[0])
    new_arr = [[0] * m for _ in range(n)]
    for r in range(n):
        for c in range(len(arr[r])):
            new_arr[r][c] = arr[r][c]
    
    tmp = [[0] * m for _ in range(n)]
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    for r in range(n):
        for c in range(m):
            if new_arr[r][c] <= 0:
                continue
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < n and 0 <= nc < m:
                    if new_arr[nr][nc] > 0:
                        d = abs(new_arr[r][c] - new_arr[nr][nc]) // 5
                        if d > 0:
                            if new_arr[r][c] > new_arr[nr][nc]:
                                tmp[r][c] -= d
                                tmp[nr][nc] += d
    # tmp의 값을 arr에 합쳐준다
    for r in range(n):
        for c in range(len(arr[r])):
            arr[r][c] += tmp[r][c]
    
            
def make_a_row():
    global arr
    new_arr = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            new_arr.append([arr[i][j]])
    arr = new_arr

def float_and_rotate_half(arr):
    for _ in range(2):
        n = len(arr)
        # 왼쪽 n/2개
        half = arr[:n//2]
        half = rotate_90(rotate_90(half))
        # 다시 반쪽에 붙인다
        arr = arr[n//2:]
        for r in range(len(half)):
            for fish in half[r]:
                arr[r].append(fish)
    return arr

def is_k():
    # 물고기가 가장 많이 들어있는 어항과 가장 적게 들어있는 어항의 물고기 수 차이가 K 이하가 되는가?
    max_fish = 0
    min_fish = float('inf')
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] > max_fish:
                max_fish = arr[i][j]
            if arr[i][j] < min_fish:
                min_fish = arr[i][j]
    return max_fish - min_fish <= k


turn = 1
while True:
    add_fish()
    stack_bowl()
    arr = float_and_rotate(arr)
    adjust_fish()
    make_a_row()
    arr = float_and_rotate_half(arr)
    adjust_fish()
    make_a_row()
    if is_k():
        break
    turn += 1


print(turn)