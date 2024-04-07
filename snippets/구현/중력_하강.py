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

print('=' * 10, "초기 arr", "=" * 10)
print_square(arr)
print('=' * 10, "gravity() 실행 후", '=' * 10)
gravity()
print_square(arr)
            
    
