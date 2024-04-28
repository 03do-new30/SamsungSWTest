from collections import deque

n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

purifiers = []
# 공기청정기를 찾는다
for r in range(n):
    if arr[r][0] == -1:
        purifiers.append((r, 0))

# 확산
def spread():
    q = deque()
    # 미세먼지가 있는 위치 저장
    for r in range(n):
        for c in range(m):
            if arr[r][c] > 0:
                q.append((r, c))
    # 더해질 미세먼지들을 저장
    added = [[0] * m for _ in range(n)]
    while q:
        r, c = q.popleft()
        # 원래 미세먼지의 양
        dust = arr[r][c]
        # 확산되는 미세먼지의 양
        spread_dust = dust // 5
        # 확산되는 방향의 개수
        cnt = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] >= 0:
                    added[nr][nc] += spread_dust
                    cnt += 1
        # 남은 미세먼지의 양으로 만듦
        added[r][c] -= spread_dust * cnt
    # spread와 합쳐서 확산 후의 결과를 만듦
    for r in range(n):
        for c in range(m):
            if arr[r][c] == -1:
                continue
            arr[r][c] += added[r][c]

# 공기청정기 작동
def purify():
    # 위쪽 공기청정기
    ur, uc = purifiers[0]
    udr = [0, -1, 0, 1]
    udc = [1, 0, -1, 0]
    saved_val = 0
    for i in range(4):
        while 0 <= ur + udr[i] < n and 0 <= uc + udc[i] < m:
            nr = ur + udr[i]
            nc = uc + udc[i]
            if arr[nr][nc] == -1:
                break
            tmp = arr[nr][nc]
            arr[nr][nc] = saved_val
            saved_val = tmp
            ur = nr; uc = nc # update

    # 아래쪽 공기청정기
    lr, lc = purifiers[1]
    ldr = [0, 1, 0, -1]
    ldc = [1, 0, -1, 0]
    saved_val = 0
    for i in range(4):
        while 0 <= lr + ldr[i] < n and 0 <= lc + ldc[i] < m:
            nr = lr + ldr[i]
            nc = lc + ldc[i]
            if arr[nr][nc] == -1:
                break
            tmp = arr[nr][nc]
            arr[nr][nc] = saved_val
            saved_val = tmp
            lr = nr; lc = nc # update

while t > 0:
    spread()

    purify()
    
    t -= 1

# 미세먼지의 양
answer = 0
for r in range(n):
    for c in range(m):
        if arr[r][c] > 0:
            answer += arr[r][c]
print(answer)
    