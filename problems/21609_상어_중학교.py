from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

score = 0

def bfs(r, c, visited):

    q = deque([(r, c)])
    visited[r][c] = True

    # 무지개 블록의 방문을 처리
    rainbow_visited = [[False] * n for _ in range(n)]
    # 무지개블록 수
    rainbow_cnt = 0
    # 그룹에 속한 블록 수
    cnt = 0
    # 기준 블록의 색깔
    color = arr[r][c]

    # 지금까지 블록에 속했던 좌표들
    history = []
    
    while q:
        r, c = q.popleft()
        history.append((r, c))
        cnt += 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                # 검은색 블록은 포함되면 안된다
                if arr[nr][nc] == -1:
                    continue
                # 무지개 블록인 경우
                if arr[nr][nc] == 0 and not rainbow_visited[nr][nc]:
                    rainbow_cnt += 1
                    q.append((nr, nc))
                    rainbow_visited[nr][nc] = True
                # 기준 블록의 컬러와 같은 경우
                elif arr[nr][nc] == color and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True
    return cnt, rainbow_cnt, history

def gravity():
    # print("### gravity")
    # print('before')
    # for row in arr:
    #     print(row)
    for c in range(n):
        for r in range(n-1, -1, -1):
            # 검은색 블록은 이동하지 않는다!
            if arr[r][c] == -1:
                continue
            if arr[r][c] != -100: # 빈칸
                nr = r
                while nr + 1 < n and arr[nr+1][c] == -100:
                    nr += 1
                if nr > r:
                    arr[nr][c] = arr[r][c]
                    arr[r][c] = -100
    # print('after')
    # for row in arr:
    #     print(row)

def reverse_clock_90():
    global arr
    # print("\n### 90도 반시계방향 회전")
    # 격자가 90도 반시계 방향으로 회전한다
    new_arr = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            new_arr[n-1-c][r] = arr[r][c]
    arr = [row[:] for row in new_arr]
    # for row in arr:
    #     print(row)


def auto_play():
    visited = [[False] * n for _ in range(n)]
    # 기준 블록별로 속한 블록의 좌표 저장
    history_dict = dict()
    # 기준 블록 저장
    groups = [] # (기준블록 r, 기준블록 c, cnt, rainbow_cnt) 저장
    for r in range(n):
        for c in range(n):
            # 방문하지 않은 기준 블록을 찾는다.
            # 검정색이나 무지개 블록은 기준 블록이 될 수 없다.
            if arr[r][c] == -1 or arr[r][c] == 0:
                continue
            # 빈칸도 기준 블록이 될 수 없다.
            if arr[r][c] == -100:
                continue
            if not visited[r][c]:
                cnt, rainbow_cnt, history = bfs(r, c, visited)
                if cnt >= 2:
                    groups.append((r, c, cnt, rainbow_cnt))
                    history_dict[(r, c)] = history
    # 블록 그룹이 존재하지 않는다면 오토플레이를 하지 않는다
    if len(groups) == 0:
        return False
    
    # 1. 크기가 가장 큰 블록 그룹을 찾는다
    groups.sort(key = lambda x : (-x[2], -x[3], -x[0], -x[1]))
    biggest_group = groups[0]

    # 2. 1에서 찾은 블록 그룹의 모든 블록을 제거한다
    r, c, cnt, rainbow_cnt = biggest_group
    del_blocks = history_dict[(r, c)]
    for del_r, del_c in del_blocks:
        arr[del_r][del_c] = -100 
    # 블록 그룹에 포함된 블록 수만큼 점수를 얻는다
    global score
    score += cnt ** 2

    # 3. 격자에 중력이 작용한다.
    gravity()

    # 4. 격자가 90도 반시계 방향으로 회전한다
    reverse_clock_90()

    # 5. 다시 격자에 중력이 작용한다
    gravity()

    return True

continue_auto_play = True

while continue_auto_play:
    continue_auto_play = auto_play()
print(score)