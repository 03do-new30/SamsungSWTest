from collections import deque

n, m = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]

spaces = [] # 빈 공간의 좌표
viruses = [] # 바이러스의 좌표
for r in range(n):
    for c in range(m):
        if arr[r][c] == 2:
            viruses.append((r, c))
        elif arr[r][c] == 0:
            spaces.append((r, c))

# 빈 공간의 좌표에서 3개를 골라 벽을 세우는 조합을 만들어본다
combinations = []
def make_combinations(n, arr, current, index):
    if len(current) == n:
        combinations.append(current)
        return
    for i in range(index, len(arr)):
        make_combinations(n, arr, current + [arr[i]], i + 1)

def bfs(arr, viruses):
    q = deque(viruses)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    n = len(arr); m = len(arr[0])
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == 0:
                    arr[nr][nc] = 2
                    q.append((nr, nc))

make_combinations(3, spaces, [], 0)
answer = 0
for combi in combinations:
    new_arr = [row[:] for row in arr]
    for r, c in combi:
        new_arr[r][c] = 1 # 벽을 세운다
    # 바이러스를 퍼뜨린다
    bfs(new_arr, viruses)
    # 안전 영역의 크기를 구한다
    safe_area = 0
    for r in range(n):
        for c in range(m):
            if new_arr[r][c] == 0:
                safe_area += 1
    if safe_area > answer:
        answer = safe_area

print(answer)