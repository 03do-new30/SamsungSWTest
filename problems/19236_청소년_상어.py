from copy import deepcopy

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

arr = []
for _ in range(4):
    tmp = list(map(int, input().split()))
    row = []
    for i in range(0, len(tmp), 2):
        row.append([tmp[i], tmp[i+1]-1])
    arr.append(row)

answer = 0

def dfs(arr, sr, sc, stomach):
    global answer
    # 먹고 물고기 번호 비교
    stomach += arr[sr][sc][0]
    if answer < stomach:
        answer = stomach
    arr[sr][sc][0] = 0

    # 물고기 이동
    for id in range(1, 17):
        fr, fc = -1, -1
        for r in range(4):
            for c in range(4):
                if arr[r][c][0] == id:
                    fr = r; fc = c
                    break
        if fr == -1 and fc == -1:
            continue
        
        fd = arr[fr][fc][1]

        # 이동 가능한 방향이 될때까지 전환한다
        for i in range(8):
            nd = (fd + i) % 8
            nr = fr + dr[nd]
            nc = fc + dc[nd]
            if not(0 <= nr < 4 and 0 <= nc < 4) or (nr == sr and nc == sc):
                continue
            # 이동 가능한 경우
            arr[fr][fc][1] = nd
            arr[fr][fc], arr[nr][nc] = arr[nr][nc], arr[fr][fc]
            break
    
    # 상어 이동
    sd = arr[sr][sc][1]
    for i in range(1, 5):
        new_sr = sr + dr[sd] * i
        new_sc = sc + dc[sd] * i
        if 0 <= new_sr < 4 and 0 <= new_sc < 4:
            if arr[new_sr][new_sc][0] > 0:
                new_arr = deepcopy(arr)
                dfs(new_arr, new_sr, new_sc, stomach)

dfs(arr, 0, 0, 0)
print(answer)