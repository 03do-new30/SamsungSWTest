dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# 구름의 위치
cloud = [[0] * n for _ in range(n)]
cloud[n-1][0] = cloud[n-1][1] = cloud[n-2][0] = cloud[n-2][1] = 1

# 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수를 구한다
def check_diagonal(arr, r, c):
    d_idx = [1, 3, 5, 7]
    cnt = 0
    for idx in d_idx:
        nr = r + dr[idx]
        nc = c + dc[idx]
        if 0 <= nr < n and 0 <= nc < n:
            if arr[nr][nc] > 0:
                cnt += 1
    return cnt

for _ in range(m):
    d, s = map(int, input().split())
    d -= 1
    # 모든 구름이 d 방향으로 s칸 이동한다
    new_cloud = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if cloud[r][c] > 0:
                nr = r + dr[d] * s
                nc = c + dc[d] * s
                # print("nr:", nr, "nc:", nc)

                while nr < 0:
                    nr += n
                while nr >= n:
                    nr -= n
                while nc < 0:
                    nc += n
                while nc >= n:
                    nc -= n
                # print("--> nr:", nr, "nc:", nc)
                new_cloud[nr][nc] = cloud[r][c]
    # 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다
    for r in range(n):
        for c in range(n):
            if new_cloud[r][c] > 0:
                arr[r][c] += 1
    # 구름이 모두 사라진다
    cloud = [[0] * n for _ in range(n)]
    # 물이 증가한 칸 (r, c)에 물복사 마법을 시전한다.
    for r in range(n):
        for c in range(n):
            if new_cloud[r][c] > 0:
                # 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수
                cnt = check_diagonal(arr, r, c)
                arr[r][c] += cnt
    # 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    for r in range(n):
        for c in range(n):
            if arr[r][c] >= 2:
                if new_cloud[r][c] > 0:
                    continue
                arr[r][c] -= 2
                cloud[r][c] = 1

answer = 0
for row in arr:
    answer += sum(row)
print(answer)