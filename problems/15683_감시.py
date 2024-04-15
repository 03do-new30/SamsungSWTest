from collections import deque

n, m = map(int, input().split())
arr = [list((map(int, input().split()))) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# directions[i] = i번 cctv의 감시 방향을 저장한 리스트
directions = [
    [],
    [(0,), (1,), (2,), (3,)],
    [(0, 1), (2, 3)],
    [(0, 2), (0, 3), (1, 2), (1, 3)],
    [(0, 1, 2), (0, 1, 3), (1, 2, 3), (0, 2, 3)],
    [(0, 1, 2, 3)]
]
# cctv의 좌표와 타입을 저장한다
cctvs = []
for r in range(n):
    for c in range(m):
        if 1 <= arr[r][c] <= 5:
            cctvs.append((r, c, arr[r][c]))

answer = n * m # 사각지대의 최소 크기

def dfs(idx, arr):
    
    if idx == len(cctvs):
        global answer
        # 모든 cctv 탐색 완료
        current_area = sum([row.count(0) for row in arr])
        if current_area < answer:
            answer = current_area
        return
    
    r, c, mode = cctvs[idx]

    for dirs in directions[mode]:
        new_arr = [row[:] for row in arr]
        for i in dirs:
            nr = r + dr[i]
            nc = c + dc[i]
            while 0 <= nr < n and 0 <= nc < m and arr[nr][nc] != 6:
                if new_arr[nr][nc] == 0:
                    new_arr[nr][nc] = 7 # 감시는 7로 표시
                nr += dr[i]
                nc += dc[i]
        dfs(idx + 1, new_arr)

dfs(0, arr)
print(answer)
