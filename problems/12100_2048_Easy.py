n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def move_up_down(param_arr, dr, dc):
    arr = [row[:] for row in param_arr]
    merged = [[False] * n for _ in range(n)]
    up_range = range(n)
    down_range = range(n-1, -1, -1)
    target_range = None
    if dr == 1:
        target_range = down_range
    else:
        target_range = up_range
    for r in target_range:
        for c in range(n):
            if arr[r][c] == 0:
                continue
            # print("# r:", r, 'c:', c)
            nr = r; nc = c
            updated = False
            while 0 <= nr + dr < n and 0 <= nc + dc < n and not updated:
                # print("nr:", nr, "nc:", nc)
                if arr[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc
                elif arr[nr + dr][nc + dc] == arr[r][c]:
                    if not merged[nr+dr][nc+dc]:
                        merged[nr+dr][nc+dc] = True
                        arr[nr+dr][nc+dc] *= 2
                        arr[r][c] = 0
                        updated = True
                    else:
                        break
                else:
                    break
            if not updated:
                if nr != r or nc != c:
                    arr[nr][nc] = arr[r][c]
                    arr[r][c] = 0
    return arr

def move_left_right(param_arr, dr, dc):
    arr = [row[:] for row in param_arr]
    merged = [[False] * n for _ in range(n)]
    left_range = range(n)
    right_range = range(n-1, -1, -1)
    target_range = None
    if dc == 1:
        target_range = right_range
    else:
        target_range = left_range
    for c in target_range:
        for r in range(n):
            if arr[r][c] == 0:
                continue
            # print("# r:", r, 'c:', c)
            nr = r; nc = c
            updated = False
            while 0 <= nr + dr < n and 0 <= nc + dc < n and not updated:
                # print("nr:", nr, "nc:", nc)
                if arr[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc
                elif arr[nr + dr][nc + dc] == arr[r][c]:
                    if not merged[nr+dr][nc+dc]:
                        merged[nr+dr][nc+dc] = True
                        arr[nr+dr][nc+dc] *= 2
                        arr[r][c] = 0
                        updated = True
                    else:
                        break
                else:
                    break
            if not updated:
                if nr != r or nc != c:
                    arr[nr][nc] = arr[r][c]
                    arr[r][c] = 0
    return arr

answer= 0
def solve(arr, cnt):
    global answer
    if cnt == 5:
        max_val = max(map(max, arr))
        if max_val > answer:
            answer = max_val
        return
    
    solve(move_up_down(arr, -1, 0), cnt + 1)
    solve(move_up_down(arr, 1, 0), cnt + 1)
    solve(move_left_right(arr, 0, -1), cnt + 1)
    solve(move_left_right(arr, 0, 1), cnt + 1)

solve(arr, 0)
print(answer)