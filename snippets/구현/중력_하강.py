arr = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
    [0, 0, 1],
    [0, 1, 0]
]
n = len(arr); m = len(arr[0])

def print_square(arr):
    for row in arr:
        print(row)

# 빈칸이 0이라고 할 때,
# 중력이 가해져서 0이 아닌 블록들이 아래로 하강해야하는 경우
def gravity():
    for c in range(m):
        zeros = []
        not_zeros = []
        for r in range(n):
            if arr[r][c] == 0:
                zeros.append(0)
                continue
            not_zeros.append(arr[r][c])
        new_column = zeros + not_zeros
        for r in range(n):
            arr[r][c] = new_column[r]

# 다른 방식
def other_gravity():
    for i in range(n-1):
        for j in range(m):
            p = i
            # 현재 칸이 아래로 내려갈 수 있다면 그 윗줄도 한 칸씩 연쇄적으로 내려와야 함
            while 0 <= p and arr[p][j] == 1 and arr[p+1][j] == 0:
                arr[p][j], arr[p+1][j] = arr[p+1][j], arr[p][j]
                p -= 1

print('=' * 10, "초기 arr", "=" * 10)
print_square(arr)
print('=' * 10, "gravity() 실행 후", '=' * 10)
gravity()
print_square(arr)
            


new_arr = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
    [0, 0, 1],
    [0, 1, 0]
]
print('=' * 10, "초기 arr", "=" * 10)
print_square(new_arr)
print('=' * 10, "other_gravity() 실행 후", '=' * 10)
gravity()
print_square(arr)