from collections import deque
n = int(input())
arr = [[0] * (n+1)]
for _ in range(n):
    arr.append([0] + list(map(int, input().split())))

def town(visited, r_start, r_limit, c_start, c_limit, number):
    for r in range(r_start, r_limit):
        for c in range(c_start, c_limit):
            visited[r][c] = number

def solve(x, y, d1, d2):
    visited = [[0] * (n+1) for _ in range(n+1)]
    # 5번 타운
    for d in range(d1 + 1):
        visited[x + d][y - d] = 5
    for d in range(d2 + 1):
        visited[x + d][y + d] = 5
    for d in range(d2 + 1):
        visited[x + d1 + d][y - d1 + d] = 5
    for d in range(d1 + 1):
        visited[x + d2 + d][y + d2 - d] = 5
    
    for i in range(1, n+1):
        between = []
        five_start = False
        for j in range(1, n+1):
            if visited[i][j] == 5:
                if not five_start:
                    five_start = True
                else:
                    for r, c in between:
                        visited[r][c] = 5
                    break
            if five_start:
                between.append((i, j))

    # 1번 타운
    town1 = 0
    for r in range(1, x + d1):
        for c in range(1, y + 1):
            if visited[r][c] != 0:
                continue
            visited[r][c] = 1
            town1 += arr[r][c]
    # 2번 타운
    town2 = 0
    for r in range(1, x + d2 + 1):
        for c in range(y+1, n+1):
            if visited[r][c] != 0:
                continue
            visited[r][c] = 2
            town2 += arr[r][c]
    # 3번 타운
    town3 = 0
    for r in range(x + d1, n+1):
        for c in range(1, y - d1 + d2):
            if visited[r][c] != 0:
                continue
            visited[r][c] = 3
            town3 += arr[r][c]
    # 4번 타운
    town4 = 0
    for r in range(x + d2 + 1, n + 1):
        for c in range(y - d1 + d2, n + 1):
            if visited[r][c] != 0:
                continue
            visited[r][c] = 4
            town4 += arr[r][c]
    
    town5 = 0
    for r in range(1, n+1):
        for c in range(1, n+1):
            if visited[r][c] == 5:
                town5 += arr[r][c]

    # for row in visited:
    #     print(row)
    # print('-' * 30)
    # 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이
    towns = [town1, town2, town3, town4, town5]
    return max(towns) - min(towns)
            

points = []
for x in range(1, n+1):
    for y in range(1, n+1):
        points.append((x, y))

answer = float('inf')
for x, y in points:
    for d1 in range(1, n+1):
        for d2 in range(1, n+1):
            if 1 <= x < x + d1 + d2 <= n and 1 <= y - d1 < y < y + d2 <= n:
                ret = solve(x, y, d1, d2)
                if ret < answer:
                    answer = ret
print(answer)