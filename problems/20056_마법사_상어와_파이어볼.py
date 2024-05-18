from math import floor

n, m, k = map(int, input().split())
arr = [[[] for __ in range(n)] for _ in range(n)]
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(m):
    r, c, mass, speed, direction = map(int, input().split())
    r -= 1; c -= 1
    arr[r][c].append((mass, speed, direction))

def fire_move():
    global arr
    # 1. 모든 파이어볼이 자신의 방향 d로 속력 s칸만큼 이동한다
    new_arr = [[[] for __ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if len(arr[r][c]) <= 0:
                continue
            for mass, speed, direction in arr[r][c]:
                nr = r + dr[direction] * speed
                nc = c + dc[direction] * speed
                while nr < 0:
                    nr += n
                while nr >= n:
                    nr -= n
                while nc < 0:
                    nc += n
                while nc >= n:
                    nc -= n
                new_arr[nr][nc].append((mass, speed, direction))
    # 2개 이상의 파이어볼이 있는 칸 검사
    arr = [[[] for __ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if len(new_arr[r][c]) >= 2:
                fireballs = new_arr[r][c]
                new_mass = 0
                new_speed = 0
                dir_all_odd = True
                dir_all_even = True
                for mas, spe, dir in fireballs:
                    new_mass += mas
                    new_speed += spe
                    if dir % 2 == 0:
                        dir_all_odd = False
                    else:
                        dir_all_even = False
                new_mass = floor(new_mass / 5)
                new_speed = floor(new_speed / len(fireballs))
                if dir_all_even or dir_all_odd:
                    new_directions = [0, 2, 4, 6]
                else:
                    new_directions = [1, 3, 5, 7]
                
                # 질량이 0인 파이어볼은 소멸되어 없어진다
                if new_mass <= 0:
                    continue

                for new_dir in new_directions:
                    arr[r][c].append((new_mass, new_speed, new_dir))


            elif len(new_arr[r][c]) == 1:
                arr[r][c].append(new_arr[r][c][0])

for _ in range(k):
    fire_move()

answer = 0
for r in range(n):
    for c in range(n):
        if len(arr[r][c]) > 0:
            for fireball in arr[r][c]:
                answer += fireball[0]
print(answer)