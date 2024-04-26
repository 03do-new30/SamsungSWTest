from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(arr, baby_r, baby_c, size):
    visited = [[False] * n for _ in range(n)]
    visited[baby_r][baby_c] = True
    q = deque()
    q.append((baby_r, baby_c, 0))

    # 먹을 수 있는 물고기의 좌표를 저장해둔다
    fishes = []

    while q:
        r, c, distance = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc]:
                    # 아기상어보다 크기가 작거나 같아야 지나갈 수 있음
                    if arr[nr][nc] <= size:
                        visited[nr][nc] = True
                        q.append((nr, nc, distance + 1))
                        # 만약 아기상어보다 크기가 작다면 먹을 수 있는 물고기이므로 저장한다. 이때 0은 빈 칸임에 주의한다
                        if 0 < arr[nr][nc] < size:
                            fishes.append((distance + 1, nr, nc))
    return fishes

cnt = 0 # 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간
size = 2 # 아기 상어의 크기
stomach = 0 # 아기 상어가 먹은 물고기 개수
# 아기상어의 위치
baby_loc = (-1, -1)
for r in range(n):
    for c in range(n):
        if arr[r][c] == 9:
            baby_loc = (r, c)
            break
arr[baby_loc[0]][baby_loc[1]] = 0
while True:
    fishes = bfs(arr, baby_loc[0], baby_loc[1], size)
    if not fishes:
        break

    # fishes 정렬 기준 = 근거리, r 오름차순, c 오름차순
    fishes.sort(key = lambda x : (x[0], x[1], x[2]))

    # 아기상어가 물고기를 먹는다
    eat_dist, eat_r, eat_c = fishes[0]
    baby_loc = (eat_r, eat_c)
    arr[eat_r][eat_c] = 0
    stomach += 1
    # 만약 자기 크기와 같은 수의 물고기를 먹으면 크기가 증가
    if stomach == size:
        stomach = 0
        size += 1
    cnt += eat_dist # 한칸 이동시 1만큼 시간 증가, eat_dist만큼 시간이 증가

print(cnt)