# 정사각형 회전
arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
n = 4

def clock_90(arr):
    new_arr = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            new_arr[c][n-1-r] = arr[r][c]
    return new_arr

def clock_180(arr):
    new_arr = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            new_arr[n-1-r][n-1-c] = arr[r][c]
    return new_arr

def clock_270(arr):
    new_arr = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            new_arr[n-1-c][r] = arr[r][c]
    return new_arr

def print_square(arr):
    for row in arr:
        print(row)

print('=' * 10, "정사각형", '=' * 10)
print_square(arr)
print('=' * 10, "시계방향 90도 회전", '=' * 10)
print_square(clock_90(arr))
print('=' * 10, "시계방향 180도 회전", '=' * 10)
print_square(clock_180(arr))
print('=' * 10, "시계방향 270도 회전", '=' * 10)
print_square(clock_270(arr))

