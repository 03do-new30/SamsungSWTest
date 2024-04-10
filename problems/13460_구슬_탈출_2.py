from collections import deque

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
drs = [0, 0, -1, 1]
dcs = [-1, 1, 0, 0]

# visited[red_r][red_c][blue_r][blue_c]
visited = [[[[False] * m for _ in range(n)] for __ in range(m)] for ___ in range(n)]

answer = -1

def move(r, c, dr, dc):
    steps = 0 # 구슬이 움직인 칸 수
    while arr[r][c] != 'O' and arr[r+dr][c+dc] != '#':
        r += dr
        c += dc
        steps += 1
    return r, c, steps
    
red = None; blue = None
for r in range(n):
    for c in range(m):
        if arr[r][c] == 'R':
            red = (r, c)
        elif arr[r][c] == 'B':
            blue = (r, c)
        if red is not None and blue is not None:
            break

def bfs(rr, rc, br, bc):
    visited[rr][rc][br][bc] = True
    q = deque()
    q.append((rr, rc, br, bc, 1))

    while q:
        rr, rc, br, bc, cnt = q.popleft()
        
        if cnt > 10:
            break

        for i in range(4):
            new_rr, new_rc, red_steps = move(rr, rc, drs[i], dcs[i])
            new_br, new_bc, blue_steps = move(br, bc, drs[i], dcs[i])

            # 파란 구슬이 구멍에 빠지는가?
            if arr[new_br][new_bc] != 'O':
                # 빨간 구슬이 구멍에 빠지는가?
                if arr[new_rr][new_rc] == 'O':
                    print(cnt)
                    return
            
                # 빨간 구슬과 파란 구슬의 좌표가 같을 때
                if new_rr == new_br and new_rc == new_bc:
                    # steps가 더 적은 것이 먼저 도착한다
                    # step이 더 많은 구슬을 back
                    if red_steps < blue_steps:
                        new_br -= drs[i]
                        new_bc -= dcs[i]
                    else:
                        new_rr -= drs[i]
                        new_rc -= dcs[i]

                # 방문 여부 검사
                if not visited[new_rr][new_rc][new_br][new_bc]:
                    visited[new_rr][new_rc][new_br][new_bc] = True
                    q.append((new_rr, new_rc, new_br, new_bc, cnt + 1))
    # 실패
    print(-1)

bfs(red[0], red[1], blue[0], blue[1])

"""
9 5
#####
#R..#
#.#.#
#...#
###.#
#B#.#
###.#
#O..#
#####
"""