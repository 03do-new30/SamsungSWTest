from collections import deque

n, k = map(int, input().split())
color = [list(map(int, input().split())) for _ in range(n)]
board = [[deque() for __ in range(n)] for _ in range(n)]

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

player_dir = dict()
for player_id in range(1, k+1):
    r, c, d = map(int, input().split())
    r -= 1; c -= 1; d -= 1
    player_dir[player_id] = d
    board[r][c].append(player_id)

def find(id):
    for r in range(n):
        for c in range(n):
            if id in board[r][c]:
                return r, c
    return -1, -1

def get_upper_players(id, r, c):
    stay = deque()
    ret = deque()
    id_found = False
    while board[r][c]:
        current_id = board[r][c].popleft()
        if current_id == id:
            id_found = True
        if id_found:
            ret.append(current_id)
        else:
            stay.append(current_id)
    board[r][c] = stay
    return ret

            
def full_players(r, c):
    return len(board[r][c]) >= 4

def get_counter_dir(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    else:
        return 2

def white_move(id, r, c, nr ,nc):
    players = get_upper_players(id, r, c)
    while players:
        board[nr][nc].append(players.popleft())
    return full_players(nr, nc)
    
def red_move(id, r, c, nr, nc):
    players = get_upper_players(id, r, c)
    while players:
        board[nr][nc].append(players.pop())
    return full_players(nr, nc)

def blue_move(id, r, c):
    # 반대 방향으로 설정
    player_dir[id] = get_counter_dir(player_dir[id])
    i = player_dir[id]
    nr = r + dr[i]
    nc = c + dc[i]
    if 0 <= nr < n and 0 <= nc < n:
        if color[nr][nc] == 0:
            white_move(id, r, c, nr, nc)
        elif color[nr][nc] == 1:
            red_move(id, r, c, nr, nc)
        return full_players(nr, nc)
    return full_players(r, c)

answer = 0
for turn in range(1, 1001):
    full_turn = False
    for id in range(1, k + 1):
        if full_turn:
            break
        r, c = find(id)
        d = player_dir[id]
        nr = r  + dr[d]
        nc = c  + dc[d]

        if 0 <= nr < n and 0 <= nc < n:
            if color[nr][nc] == 0:
                is_full_players = white_move(id, r, c, nr, nc)
            elif color[nr][nc] == 1:
                is_full_players = red_move(id, r, c, nr, nc)
            else:
                is_full_players =blue_move(id, r, c)
        else:
            is_full_players = blue_move(id, r, c)
        
        if is_full_players:
            full_turn = True
    if full_turn:
        answer = turn
        break
if answer <= 0:
    answer = -1
print(answer)
        
        