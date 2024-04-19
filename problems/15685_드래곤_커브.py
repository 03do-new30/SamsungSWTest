n = int(input())
dragons = [list(map(int, input().split())) for _ in range(n)]
dr = [0, -1, 0, 1] # 우, 상, 좌, 하
dc = [1, 0, -1, 0]
arr = [[False] * 101 for _ in range(101)]

# 
def next_generation(directions):
    new_dirs = []
    # 0: (0, 1)
    # 1: (0, 1) 
    #       + (-1, 0)
    # 2: (0, 1), (-1, 0) 
    #       + (0, -1), (-1, 0)
    # 3: (0, 1), (-1, 0), (0, -1), (-1, 0)
    #       + (0, -1), (1, 0), (0, -1), (-1, 0)
    # n세대 방향: (n-1) 세대의 방향들을 역순으로 바꾼 뒤 (r, c) -> (-c, r)이 되는 규칙
    for i in range(len(directions)-1, -1, -1):
        r, c = directions[i]
        new_dirs.append((-c, r))
    return new_dirs

for x, y, d, g in dragons:
    # 드래곤 커브의 진행 방향을 저장한다
    # directions[i] = i세대의 진행 방향
    directions =[(dr[d],dc[d])]
    # 세대만큼 진행
    while g > 0:
        directions += next_generation(directions)
        # print("directions:", directions)
        g -= 1
    # 격자에 표시
    # 맨 처음 시작점 표시
    arr[y][x] = True
    # 격자에 표시한다
    # 드래곤 커브에 포함되는 꼭지점은 True로 표시
    for row_dir, col_dir, in directions:
        arr[y+row_dir][x+col_dir] = True
        y += row_dir
        x += col_dir

    

# 정사각형의 개수를 구한다
answer = 0
for r in range(100):
    for c in range(100):
        if not arr[r][c]:
            continue
        if arr[r][c] == arr[r][c+1] == arr[r+1][c+1] == arr[r+1][c] == True:
            answer += 1
print(answer)