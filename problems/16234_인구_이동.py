from collections import deque
n, left, right = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def bfs(arr, r, c, flag, check):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    q = deque([(r, c)])
    check[r][c] = flag

    opened = False # 국경이 하나라도 열렸는지

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if check[nr][nc] == 0:
                    if left <= abs(arr[r][c] - arr[nr][nc]) <= right:
                        # 국경을 공유할 수 있다
                        q.append((nr, nc))
                        check[nr][nc] = flag
                        if not opened:
                            opened = True
    return opened


# 국경선 공유 여부 체크
def check_union(arr):
    # 0은 방문하지 않았다는 의미
    # 국경선을 공유하는 나라들은 같은 숫자를 가짐
    check = [[0] * n for _ in range(n)]

    flag = 1 # 국경선을 공유하는 나라들에 붙여줄 번호

    opened = False # 국경이 열렸는지
    for r in range(n):
        for c in range(n):
            if check[r][c] == 0:
                bfs_opened = bfs(arr, r, c, flag, check)
                
                if bfs_opened:
                    opened = True
                
                flag += 1 # 다음 플래그는 하나 더 증가
    
    return opened, check

cnt = 0 # 인구 이동이 발생하는 일 수
while True:
    opened, check = check_union(arr)
    if not opened:
        break
    # 연합대로 국가들을 정리해본다
    unions = dict()
    for r in range(n):
        for c in range(n):
            union_id = check[r][c]
            if union_id in unions:
                unions[union_id].append((r, c))
            else:
                unions[union_id] = [(r, c)]
    # 인구이동을 시작한다
    for union_id in unions:
        tmp_ppl = 0
        for r, c in unions[union_id]:
            tmp_ppl += arr[r][c]
        people = tmp_ppl // len(unions[union_id])
        for r, c in unions[union_id]:
            arr[r][c] = people
    # 일수가 증가한다
    cnt += 1
    
print(cnt)