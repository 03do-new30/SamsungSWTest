from collections import deque

n, m, oil = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
start_r, start_c = map(int, input().split())
start_r -= 1; start_c -= 1
passengers = []
for _ in range(m):
    r1, c1, r2, c2 = map(int, input().split())
    r1 -= 1; c1 -= 1; r2 -= 1; c2 -= 1
    passengers.append((r1, c1, r2, c2))

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
INF = float('inf')

# (start_r, start_c)를 기준으로 모든 좌표에 대해 최단거리를 구한다
def get_dist_arr(start_r, start_c):
    q = deque([(start_r, start_c, 0)])
    dist_arr = [[INF] * n for _ in range(n)]
    dist_arr[start_r][start_c] = 0
    while q:
        r, c, cnt = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if arr[nr][nc] == 0 and dist_arr[nr][nc] == INF:
                    dist_arr[nr][nc] = cnt + 1
                    q.append((nr, nc, cnt + 1))
    return dist_arr

# (r1, c1), (r2, c2)로 가는 최단거리를 구한다
def get_min_dist(r1, c1, r2, c2):
    q = deque([(r1, c1, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[r1][c1] = True
    while q:
        r, c, cnt = q.popleft()
        if r == r2 and c == c2:
            return cnt
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if arr[nr][nc] == 0 and not visited[nr][nc]:
                    q.append((nr, nc, cnt + 1))
                    visited[nr][nc] = True
    return INF

# 승객 체크
passenger_check = [False] * m

success = True

for _ in range(m):
    # (start_r, start_c)를 기준으로 각 좌표별 최단거리를 저장한 dist_arr
    dist_arr = get_dist_arr(start_r, start_c)
    
    # 최단거리로 태우러 갈 수 있는 승객을 체크한다
    min_dist = INF
    candidates = []
    for i in range(m):
        if passenger_check[i]:
            continue
        p_r = passengers[i][0]
        p_c = passengers[i][1]
        p_dist = dist_arr[p_r][p_c]
        if min_dist > p_dist:
            min_dist = p_dist
            candidates = [(p_r, p_c, i)]
        elif min_dist == p_dist:
            candidates.append((p_r, p_c, i))
    
    candidates.sort(key = lambda x : (x[0], x[1]))
    p_r, p_c, p_idx = candidates[0]

    passenger_check[p_idx] = True

    # oil check
    if oil - min_dist < 0:
        success = False
        break
    oil -= min_dist

    # 승객의 목적지로 이동하는 최단거리를 구한다
    goal_r = passengers[p_idx][2]
    goal_c = passengers[p_idx][3]
    goal_dist = get_min_dist(p_r, p_c, goal_r, goal_c)

    # oil check
    if oil - goal_dist < 0:
        success = False
        break

    oil -= goal_dist
    oil += goal_dist * 2

    # update
    start_r = goal_r
    start_c = goal_c

if success:
    print(oil)
else:
    print(-1)