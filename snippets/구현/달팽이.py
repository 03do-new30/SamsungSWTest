arr = [[0] * 5 for _ in range(5)]

def tornado():
    global arr
    d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    y = len(arr) // 2
    x = len(arr) // 2
    num = 0 # 칸에 채워 넣을 값
    dist = 1
    d_idx = 0 # 서, 남, 동, 북 순서
    move_count = 0 # 2가 되면 dist 길이가 1 늘어나고 move_count는 다시 0으로 초기화된다
    while True:
        for _ in range(dist):
            dy, dx = d[d_idx]
            ny = dy + y
            nx = dx + x
            if (ny, nx) == (0, -1): # 토네이도가 모두 끝나고 나서의 위치
                return
            num += 1
            arr[ny][nx] = num
            y = ny
            x = nx
        move_count += 1
        d_idx = (d_idx + 1) % 4
        if move_count == 2:
            dist += 1
            move_count = 0
tornado()
for row in arr:
    print(row)