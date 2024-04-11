from collections import deque

n, m = map(int, input().split())
# d; 0 = 북쪽; 1 = 동; 2 = 남; 3 = 서
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]

# (0, 1) -> (-1, 0) -> (0, -1) -> (1, 0)
def reverse_clock_90(dr, dc):
    return (-dc, dr)

dr = drs[d]; dc = dcs[d] # 방향을 나타내는 dr, dc

cnt = 0
cleaned = [[False] * m for _ in range(n)]

while True:
    # 현재 칸이 아직 청소되지 않은 경우 현재 칸을 청소
    if arr[r][c] == 0 and not cleaned[r][c]:
        cleaned[r][c] = True
        cnt += 1

    all_cleaned = True
    for i in range(4):
        nr = r + drs[i]; nc = c + dcs[i]
        if 0 <= nr < n and 0 <= nc < m:
            if arr[nr][nc] == 0 and not cleaned[nr][nc]:
                all_cleaned = False
                break
    
    if all_cleaned:
        # print(" 청소되지 않은 빈 칸이 없다 ❌❌")
        # 한 칸 후진
        nr = r - dr; nc = c - dc
        if 0 <= nr < n and 0 <= nc < m:
            if arr[nr][nc] == 1:
                # print(" 벽이라 작동할 수 없다")
                break
            # print(" ", dr, dc, "방향으로 후진")
            r = nr; c = nc
            continue
        else:
            # print(" 작동할 수 없다")
            break
    else:
        # print(" 청소되지 않은 빈 칸이 있다 ⭕️⭕️")
        for _ in range(4):
            # 반시계 방향으로 90도 회전한다
            dr, dc = reverse_clock_90(dr, dc)
            # 앞쪽 칸이 청소되지 않은 빈칸인 경우 한 칸 전진한다
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == 0 and not cleaned[nr][nc]:
                    r = nr; c = nc
                    break

print(cnt)