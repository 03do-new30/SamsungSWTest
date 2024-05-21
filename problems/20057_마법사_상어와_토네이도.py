from math import floor

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 모래가 흩날리는 방향
spread_sand = [[0] * 5 for _ in range(5)]
spread_sand[0][2] = spread_sand[4][2] = 0.02
spread_sand[1][1] = spread_sand[3][1] = 0.1
spread_sand[1][2] = spread_sand[3][2] = 0.07
spread_sand[1][3] = spread_sand[3][3] = 0.01
spread_sand[2][0] = 0.05
spread_sand[2][1] = 100 # alpha

def clock_90(spread_sand):
    new_spread_sand = [[0] * 5 for _ in range(5)]
    for r in range(5):
        for c in range(5):
            new_spread_sand[c][4-r] = spread_sand[r][c]
    return new_spread_sand

up_spread_sand = clock_90(spread_sand)
right_spread_sand = clock_90(up_spread_sand)
down_spread_sand = clock_90(right_spread_sand)

def get_spread_sand(dr, dc):
    if dr == 0 and dc == -1:
        return spread_sand
    if dr == 0 and dc == 1:
        return right_spread_sand
    if dr == -1 and dc == 0:
        return up_spread_sand
    return down_spread_sand

# 격자 밖으로 나간 모래의 양
answer = 0

def in_bound(r, c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False

# 토네이도의 이동
# (r, c) = 토네이도가 시작되는 중심
tornado_dr = [0, 1]
tornado_dc = [-1, 0]
def tornado(r, c, arr):
    # 방문하는 좌표 순서
    orders = []
    speed = 1
    speed_cnt = 0
    idx = 0
    while in_bound(r, c):
        orders.append((r, c))
        if speed_cnt == speed:
            idx += 1
        elif speed_cnt == speed * 2:
            # 방향 전환
            for i in range(2):
                tornado_dr[i] *= -1
                tornado_dc[i] *= -1
            # speed 증가
            speed += 1
            # 초기화
            speed_cnt = 0
            idx = 0
        
        nr = r + tornado_dr[idx]
        nc = c + tornado_dc[idx]
        speed_cnt += 1

        # (r, c) -> (nr, nc) 로 모래를 뿌린다
        sand_info = get_spread_sand(tornado_dr[idx], tornado_dc[idx])

        # (nr, nc)에 있었던 모래의 양
        original = arr[nr][nc]
        # 알파칸에 들어갈 모래의 양
        alpha_amount = original
        # 알파칸의 방향
        alpha_dr = 0; alpha_dc = 0
        
        if original > 0:
            # 원래 (nr, nc)에 있던 모래 비워준다
            arr[nr][nc] = 0
            # print("r:", r, "c:", c, '-> nr:', nr, "nc:", nc)
            for x in range(5):
                for y in range(5):
                    if sand_info[x][y] == 0:
                        continue
                    # 퍼질 모래의 방향
                    sand_dr = x - 2
                    sand_dc = y - 2
                    # 알파 칸이라면, 방향만 저장해두고 컨티뉴
                    if sand_info[x][y] == 100:
                        alpha_dr = x-2; alpha_dc = y-2
                        continue
                    # 퍼질 모래의 양
                    move_amount = floor(original * sand_info[x][y])
                    # 알파칸에 퍼질 모래의 양 계산
                    alpha_amount -= move_amount
                    # 격자의 밖으로 퍼지는 경우
                    new_sand_r = nr + sand_dr
                    new_sand_c = nc + sand_dc
                    # print("new_sand_r", new_sand_r, ", new_sand_c:", new_sand_c)
                    if not in_bound(new_sand_r, new_sand_c):
                        global answer
                        answer += move_amount
                    else:
                        arr[new_sand_r][new_sand_c] += move_amount
            # 알파칸 처리
            # 격자의 밖으로 퍼지는 경우
            new_sand_r = nr + alpha_dr
            new_sand_c = nc + alpha_dc
            if not in_bound(new_sand_r, new_sand_c):
                answer += alpha_amount
            else:
                arr[new_sand_r][new_sand_c] += alpha_amount
            # print("r:", r, "c:", c , "nr:", nr, "nc:", nc)
            # print("alpha_dr:", alpha_dr, "alpha_dc:", alpha_dc)
            # print("알파칸:", new_sand_r, new_sand_c)
            # for row in arr:
            #     print(row)
            # print('-' * 30)
            
        r = nr; c = nc

        

tornado(n//2, n//2, arr)
print(answer)