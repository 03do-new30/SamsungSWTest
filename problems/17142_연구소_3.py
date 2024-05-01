from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

viruses = []
for r in range(n):
    for c in range(n):
        if arr[r][c] == 2:
            viruses.append((r, c))

combinations = []

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def get_combinations(tmp, idx, m):
    global combinations
    if len(tmp) == m:
        combinations.append(tmp)
        return
    for i in range(idx, len(viruses)):
        get_combinations(tmp + [viruses[i]], i + 1, m)

def spread(active_viruses):
    # count[r][c] = (r, c)까지 바이러스가 도달하는 데 걸린 시간
    count = [[-1] * n for _ in range(n)]
    # remains = 바이러스가 퍼져야 할 빈칸의 개수
    remains = 0
    for r in range(n):
        for c in range(n):
            if arr[r][c] == 0:
                remains += 1
            elif arr[r][c] == 1:
                # 벽은 방문 처리
                count[r][c] = 0
    
    q = deque()
    # active_viruses 큐 및 count 처리
    for r, c in active_viruses:
        q.append((r, c, 0))
        count[r][c] = 0
    
    max_cnt = 0
    while q:
        # 주의!
        # cnt는 편의를 위해 들고있는 값이고, 진짜 (r, c)까지 바이러스가 퍼지는 데 걸리는 시간은 count[r][c]를 생각해야 함!
        # 비활성 바이러스는 count[r][c] = 0이지만, cnt값은 비활성 바이러스까지 가는 데 걸리는 시간을 들고있다!
        r, c, cnt = q.popleft()

        global answer
        # (r, c)까지 걸리는 시간인 count가 global answer보다 크다면 더 탐색할 필요 없음
        if answer > -1 and count[r][c] > answer:
            return -1

        if count[r][c] > max_cnt:
            max_cnt = count[r][c]
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if arr[nr][nc] == 1:
                    continue
                if count[nr][nc] > -1:
                    continue
                # 비활성 바이러스가 활성으로 변한다
                if arr[nr][nc] == 2:
                    q.append((nr, nc, cnt + 1))
                    # 퍼뜨리는 데 걸리는 시간이 없기 때문에 시간은 추가되지 않는다
                    count[nr][nc] = 0
                # 빈칸
                elif arr[nr][nc] == 0:
                    q.append((nr, nc, cnt + 1))
                    count[nr][nc] = cnt + 1
                    remains -= 1
    # print("cnt")
    # for row in count:
    #     print(row)
    # print("-" * 30)
    if remains > 0:
        return -1
    else:
        return max_cnt

get_combinations([], 0, m)
answer = -1
for combi in combinations:
    spread_time = spread(combi)
    if spread_time == -1:
        continue
    if answer == -1:
        answer = spread_time
    else:
        answer = min(answer, spread_time)
print(answer)