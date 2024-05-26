dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def spread_smell(smell):
    # 기존에 있던 냄새의 지속 시간을 줄여준다
    for r in range(n):
        for c in range(n):
            if len(smell[r][c]) == 0:
                continue
            tmp = []
            for id, time in smell[r][c]:
                if time - 1 <= 0:
                    continue # 사라짐
                tmp.append((id, time - 1))
            smell[r][c] = tmp
                
    # arr의 상태를 보고 smell을 퍼뜨린다
    for r in range(n):
        for c in range(n):
            if arr[r][c] > 0:
                smell[r][c].append((arr[r][c], k))

# 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동한다
def move(arr, smell, now_dir):
    new_arr = [[[] for __ in range(n) ] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if arr[r][c] > 0:
                id = arr[r][c] # 현재 상어의 아이디
                dir = now_dir[id] # 현재 보고 있는 방향
                priority = priorities[id][dir]# 방향의 우선순위

                no_smell = [] # 냄새가 없는 칸의 좌표와 방향
                my_smell = [] # 자신의 냄새가 있는 칸의 좌표와 방향

                for i in priority:
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if in_range(nr, nc):
                        if len(smell[nr][nc]) == 0:
                            no_smell.append((nr, nc, i))
                        else:
                            for smell_id, smell_time in smell[nr][nc]:
                                if id == smell_id:
                                    my_smell.append((nr, nc, i))
                
                # print("id;", id)
                # print("no_smell:", no_smell)
                # print("my_smell:", my_smell)
                if len(no_smell) > 0:
                    next_r, next_c, next_dir = no_smell[0]
                else:
                    next_r, next_c, next_dir = my_smell[0]
                new_arr[next_r][next_c].append(id)
                now_dir[id] = next_dir
    # new_arr를 arr 형태로 만들면서
    # 한 칸에 여러마리의 상어가 남아 있는지 체크한다
    for r in range(n):
        for c in range(n):
            if len(new_arr[r][c]) > 1:
                # 가장 작은 번호를 가진 상어를 제외하고 격자 밖으로 쫓겨난다
                arr[r][c] = min(new_arr[r][c])
            elif len(new_arr[r][c]) == 1:
                arr[r][c] = new_arr[r][c][0]
            else:
                arr[r][c] = 0

# 1번 상어만 격자에 남는지 체크
def only_one():
    for r in range(n):
        for c in range(n):
            if arr[r][c] > 0:
                if arr[r][c] != 1:
                    return False
    return True
    

# 상어의 방향
now_dir = dict()
tmp = list(map(int, input().split()))
for i in range(m):
    now_dir[i+1] = tmp[i]

# print("now_dir:", now_dir)

# 각 상어의 방향 우선순위
priorities = dict()
for shark_id in range(1, m+1):
    priorities[shark_id] = [[]]
    for _ in range(4):
        priorities[shark_id].append(list(map(int, input().split())))
# print("priorities:", priorities)

smell = [[[] for _ in range(n)] for __ in range(n)]
spread_smell(smell)
answer = -1
for second in range(1001):
    # print("#" * 20, second)
    if only_one():
        answer = second
        break
    move(arr, smell, now_dir)
    spread_smell(smell)
    # print("arr")
    # for row in arr:
    #     print(row)
    # print('-' * 20)
    # print("smell")
    # for row in smell:
    #     print(row)
    # print('-' * 20)
print(answer)