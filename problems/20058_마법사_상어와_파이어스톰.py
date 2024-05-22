from collections import deque

n, q = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(2**n)]

# 상어가 시전한 단계
levels = list(map(int, input().split()))

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

# 남아있는 얼음의 합
total_ice = 0
# 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
biggest_ice = 0


# 좌측 상단의 좌표가 (x, y)이고 변의 길이가 side_length인 사각형을
# 시계방향으로 90도 회전시킨다
def rotate_90(x, y, side_length):
    tmp = [[0] * side_length for _ in range(side_length)]
    for r in range(x, x + side_length):
        for c in range(y, y + side_length):
            tmp[r-x][c-y] = arr[r][c]
    new_tmp = [[0] * side_length for _ in range(side_length)]
    for r in range(side_length):
        for c in range(side_length):
            new_tmp[c][side_length - 1 - r] = tmp[r][c]
    # arr에 new_tmp의 상태를 옮긴다
    for r in range(side_length):
        for c in range(side_length):
            arr[r + x][c + y] = new_tmp[r][c]



def fire_storm(level):
    # 회전
    for r in range(0, 2**n, 2**level):
        for c in range(0, 2**n, 2**level):
            rotate_90(r, c, 2**level)
    # 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸의 얼음의 양이 1 줄어든다.
    # 얼음의 양이 줄어드는 좌표 저장
    tmp = []
    for r in range(2**n):
        for c in range(2**n):
            if arr[r][c] == 0:
                continue
            # 인접한 얼음 칸의 개수
            ice_cnt = 0
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < 2**n and 0 <= nc < 2**n:
                    if arr[nr][nc] > 0:
                        ice_cnt += 1
            # 얼음 칸 3개 이상 인접하지 않는다면 얼음의 양을 줄이기 위해 저장해둔다
            if ice_cnt >= 3:
                continue
            tmp.append((r, c))
    # 얼음의 양 줄인다
    for r, c in tmp:
        arr[r][c] -= 1


# (r, c)에서 시작되는 얼음의 크기 계산
def bfs(r, c, visited):
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    cnt = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 2**n and 0 <= nc < 2**n:
                if arr[nr][nc] > 0 and not visited[nr][nc]:
                    cnt += 1
                    q.append((nr, nc))
                    visited[nr][nc] = True
    return cnt
            


for level in levels:
    fire_storm(level)
    # for row in arr:
    #     print(row)
    # print('-' * 30)

# 남아있는 얼음의 합 계산
for r in range(2**n):
    for c in range(2**n):
        total_ice += arr[r][c]
# 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수 계산
visited = [[False] * (2**n) for _ in range(2**n)]
for r in range(2**n):
    for c in range(2**n):
        if not visited[r][c] and arr[r][c] > 0:
            size = bfs(r, c, visited)
            if size > biggest_ice:
                biggest_ice = size

print(total_ice)
print(biggest_ice)