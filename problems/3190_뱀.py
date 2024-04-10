from collections import deque

n = int(input())
arr = [[False] * n for _ in range(n)]

k = int(input())
for _ in range(k):
    r, c = map(int, input().split())
    arr[r-1][c-1] = True

l = int(input())
direction_info = [''] * 10001
for _ in range(l):
    x, direction = input().split()
    direction_info[int(x)] = direction

# (0, 1) -> (1, 0) -> (0, -1) -> (-1, 0) 오른쪽 방향 회전
# (0, 1) -> (-1, 0) -> (0, -1) -> (1, 0) -> (0, 1) 왼쪽 방향 회전
def change_dir(direction, dr, dc):
    if direction == 'D':
        return (dc, -dr)
    else: #'L'
        return (-dc, dr)

# 초기 디렉션 설정
dr = 0; dc = 1
# 초기 좌표 설정
r, c = 0, 0
snakes = deque() # 뱀의 궤적을 저장함
snakes.append((r, c))
for time in range(10001):
    if direction_info[time] != '':
        d = direction_info[time]
        dr, dc = change_dir(d, dr, dc)
    nr = r + dr
    nc = c + dc
    if 0 <= nr < n and 0 <= nc < n:
        # 사과
        if arr[nr][nc]:
            arr[nr][nc] = False # 사과가 사라짐
            # 뱀 몸을 늘려줌
            snakes.append((nr, nc))
            # 머리가 (nr, nc)에 위치
            r = nr; c = nc
        else:
            if (nr, nc) not in snakes:
                # 빈칸
                # 머리 이동
                snakes.append((nr, nc))
                r = nr; c = nc
                # 꼬리가 위치한 칸을 비워준다
                snakes.popleft()
            else:
                # 몸과 부딪힘
                print(time + 1)
                break
            
    else:
        # 벽
        print(time + 1)
        break