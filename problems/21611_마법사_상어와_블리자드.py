from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

shark_r = shark_c = n // 2

def destroy(d, s):
    r = n // 2
    c = n // 2
    while s > 0:
        r += dr[d]
        c += dc[d]
        if 0 <= r < n and 0 <= c < n:
            arr[r][c] = 0
        s -= 1

def tornado():
    orders = []
    r = n // 2
    c = n // 2
    tornado_dr = [0, 1, 0, -1]
    tornado_dc = [-1, 0, 1, 0]
    cnt = 2
    side_length = 1
    side_cnt = 0
    i = 0
    
    nr = r
    nc = c
    while 0 <= nr + tornado_dr[i] < n and 0 <= nc + tornado_dc[i] < n:
        nr += tornado_dr[i]
        nc += tornado_dc[i]
        orders.append((nr, nc))

        side_cnt += 1
        if side_cnt == side_length:
            cnt -= 1
            if cnt == 0:
                cnt = 2
                i = (i + 1) % 4
                side_length += 1
                side_cnt = 0
                continue
            side_cnt = 0
            i += 1
    return orders

# 빈 칸 채우기
def fill_empty(arr, tornado_orders):
    # 빈 칸 채우기
    beads = []
    for r, c in tornado_orders:
        beads.append(arr[r][c])
    new_beads = []
    for i in range(len(beads)):
        if beads[i] > 0:
            new_beads.append(beads[i])
    while len(new_beads) < len(beads):
        new_beads.append(0)
    # new_beads를 토네이도 순서로 arr에 넣어준다
    for i in range(len(beads)):
        r, c = tornado_orders[i]
        arr[r][c] = new_beads[i]


# 폭발
def bomb(arr, tornado_orders):
    there_was_bomb = False
    testing_number = 0
    continuity = []
    for r, c in tornado_orders:
        if arr[r][c] == 0:
            continue
        if testing_number == 0 or testing_number == arr[r][c]:
            testing_number = arr[r][c]
            continuity.append((r, c))
        else:
            if len(continuity) >= 4:
                global cnt_1, cnt_2, cnt_3
                there_was_bomb = True
                if testing_number == 1:
                    cnt_1 += len(continuity)
                elif testing_number == 2:
                    cnt_2 += len(continuity)
                else:
                    cnt_3 += len(continuity)
                # 폭발
                for bomb_r, bomb_c in continuity:
                    arr[bomb_r][bomb_c] = 0

            # 새로운 testing_number로 교체
            testing_number = arr[r][c]
            continuity = [(r, c)]
    # 남아있는 그룹들 폭파
    if len(continuity) >= 4:
        there_was_bomb = True
        if testing_number == 1:
            cnt_1 += len(continuity)
        elif testing_number == 2:
            cnt_2 += len(continuity)
        else:
            cnt_3 += len(continuity)
        # 폭발
        for bomb_r, bomb_c in continuity:
            arr[bomb_r][bomb_c] = 0

    return there_was_bomb

tornado_orders = tornado()

cnt_1 = 0
cnt_2 = 0
cnt_3 = 0
for _ in range(m):
    d, s = map(int, input().split())
    d -= 1
    destroy(d, s)
    tornado_orders = tornado()
    
    fill_empty(arr, tornado_orders)

    # 폭발
    while bomb(arr, tornado_orders):
        # 빈 칸 채우기
        fill_empty(arr, tornado_orders)
    # print("폭발 후")
    # for row in arr:
    #     print(row)
    # print('-' * 30)
    # 구슬이 변화하는 단계
    group_number = 0
    group_cnt = 0
    new_beads = []
    for r, c in tornado_orders:
        if arr[r][c] == 0:
            continue
        if group_number == 0:
            group_number = arr[r][c]
            group_cnt = 1
        elif group_number == arr[r][c]:
            group_cnt += 1
        else:
            a = group_cnt
            b = group_number
            new_beads.append(a)
            new_beads.append(b)
            
            group_number = arr[r][c]
            group_cnt = 1
    
    new_beads.append(group_cnt)
    new_beads.append(group_number)

    arr = [[0] * n for _ in range(n)]
    # new_beads에 있는 숫자들을 순서대로 arr에 넣는다
    for i in range(len(tornado_orders)):
        r, c = tornado_orders[i]
        if i >= len(new_beads):
            break
        arr[r][c] = new_beads[i]
    # print("구슬 변화 후")
    # for row in arr:
    #     print(row)
    # print('-' * 30)
    
print(cnt_1 + 2 * cnt_2 + 3 * cnt_3)


"""
3 1
0 0 0
1 0 0
1 1 0
3 1
"""