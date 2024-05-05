from collections import deque

n, m, t = map(int, input().split())
circles = [deque(map(int, input().split())) for _ in range(n)]

def bfs(r, c):
    q = deque([(r, c, circles[r][c])])
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    visited = [[False] * m for _ in range(n)]
    visited[r][c] = True
    adjacent_number = False # 인접하면서 같은 수가 있는지
    
    while q:
        r, c, num = q.popleft()
        # 끝과 끝 비교
        if c == 0:
            if not visited[r][m-1]:
                if circles[r][m-1] == num:
                    if not adjacent_number:
                        adjacent_number = True
                    visited[r][m-1] = True
                    q.append((r, m-1, num))
        if c == m-1:
            if not visited[r][0]:
                if circles[r][0] == num:
                    if not adjacent_number:
                        adjacent_number = True
                    visited[r][0] = True
                    q.append((r, 0, num))
            
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if visited[nr][nc]:
                    continue
                if circles[nr][nc] != num:
                    continue
                if circles[nr][nc] == num:
                    if not adjacent_number:
                        adjacent_number = True
                    visited[nr][nc] = True
                    q.append((nr, nc, num))
    if adjacent_number:
        for r in range(n):
            for c in range(m):
                if visited[r][c]:
                    circles[r][c] = 0
    return adjacent_number
for _ in range(t):
    x, d, k = map(int, input().split())
    i = 1
    while x * i - 1 < n:
        if d == 0:
            circles[x * i - 1].rotate(1 * k)
        else:
            circles[x * i - 1].rotate(-1 * k)
        i += 1
    
    # 원판에 수가 남아 있으면 인접하면서 수가 같은 것을 모두 찾는다
    adjacent_number_deleted = False
    for r in range(n):
        for c in range(m):
            if circles[r][c] != 0:
                status = bfs(r, c)
                if status:
                    adjacent_number_deleted = True
    # 전부 다 0인 경우
    all_zero = True
    for r in range(n):
        for c in range(m):
            if circles[r][c] != 0:
                all_zero = False
                break
    if all_zero:
        break
    
    if not adjacent_number_deleted:
        total = 0
        cnt = 0
        for r in range(n):
            for c in range(m):
                if circles[r][c] == 0:
                    continue
                total += circles[r][c]
                cnt += 1
        average = total / cnt
        for r in range(n):
            for c in range(m):
                if circles[r][c] == 0:
                    continue
                if circles[r][c] < average:
                    circles[r][c] += 1
                elif circles[r][c] > average:
                    circles[r][c] -= 1

answer = 0
for circle in circles:
    answer += sum(circle)
print(answer)