arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

def clock_90(arr):
    n = len(arr); m = len(arr[0])
    new_arr = [[0] * n for _ in range(m)] # 가로세로 길이 반대로
    for r in range(n):
        for c in range(m):
            new_arr[c][n-1-r] = arr[r][c]
    return new_arr

def clock_180(arr):
    n = len(arr); m = len(arr[0])
    new_arr = [[0] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            new_arr[n-1-r][m-1-c] = arr[r][c]
    return new_arr

def clock_270(arr):
    n = len(arr); m = len(arr[0])
    new_arr = [[0] * n for _ in range(m)] # 가로세로 길이 반대로
    for r in range(n):
        for c in range(m):
            new_arr[m-1-c][r] = arr[r][c]
    return new_arr

def print_square(arr):
    for row in arr:
        print(row)
print('=' * 10, "직사각형", '=' * 10)
print_square(arr)
print('=' * 10, "시계방향 90도 회전", '=' * 10)
print_square(clock_90(arr))
print('=' * 10, "시계방향 180도 회전", '=' * 10)
print_square(clock_180(arr))
print('=' * 10, "시계방향 270도 회전", '=' * 10)
print_square(clock_270(arr))