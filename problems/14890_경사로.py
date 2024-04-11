# https://velog.io/@eastgloss0330/%EB%B0%B1%EC%A4%80-14890-%EA%B2%BD%EC%82%AC%EB%A1%9C

n, length = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def route(r, c, dr, dc):
    # 경사로를 놓은 곳을 표시
    visited = [[False] * n for _ in range(n)]

    while 0 <= r + dr < n and 0 <= c + dc < n:
        if arr[r][c] == arr[r+dr][c+dc]:
            r += dr
            c += dc
        # 다음 블록이 낮은 블록인 경우
        elif arr[r][c] - arr[r+dr][c+dc] == 1:
            if lower_block(r, c, dr, dc, visited):
                # 경사로를 설치할 수 있음
                nr = r; nc = c
                for _ in range(length):
                    nr += dr; nc += dc
                    visited[nr][nc] = True
                # 경사로를 놓은 뒤의 블록으로 이동한다
                r = nr; c = nc
            else:
                # 경사로를 설치할 수 없음
                return False
        # 다음 블록이 높은 블록인 경우
        elif arr[r][c] - arr[r+dr][c+dc] == -1:
            # 높은 블록의 좌표를 파라미터로 넘겨준다
            if higher_block(r+dr, c+dc, dr, dc, visited):
                # 경사로를 설치할 수 있음
                nr = r + dr; nc = c + dc
                for _ in range(length):
                    nr -= dr; nc -= dc
                    visited[nr][nc] = True
                # 경사로를 놓은 뒤의 블록으로 이동한다
                r = r + dr; c = c + dc
            else:
                return False
        else:
            return False
    return True

def lower_block(r, c, dr, dc, visited):
    # (r, c)의 높이
    height = arr[r][c]
    # length개의 칸이 연속되어 있는가?
    if 0 <= r + dr * length < n and 0 <= c + dc * length < n:
        # length개의 칸의 높이가 모두 height - 1 인가?
        nr = r
        nc = c
        for _ in range(length):
            nr += dr
            nc += dc
            if arr[nr][nc] != height -1:
                return False # 경사로 놓기 실패
            if visited[nr][nc]:
                return False # 이미 경사로가 설치되어 있음
    else:
        return False
    return True

def higher_block(r, c, dr, dc, visited):
    # (r, c)의 높이
    height = arr[r][c]
    # (r, c)로부터 뒤로 length개의 칸이 연속되어 있는가?
    if 0 <= r - dr * length < n and 0 <= c - dc * length < n:
        # length개의 칸의 높이가 모두 height - 1인가?
        nr = r
        nc = c
        for _ in range(length):
            nr -= dr
            nc -= dc
            if arr[nr][nc] != height - 1:
                return False
            if visited[nr][nc]:
                return False
    else:
        return False
    return True

answer = 0
for r in range(n):
    row_result = route(r, 0, 0, 1) # 가로방향
    if row_result:
        answer += 1
for c in range(n):
    col_result = route(0, c, 1, 0) # 세로방향
    if col_result:
        answer += 1
print(answer)