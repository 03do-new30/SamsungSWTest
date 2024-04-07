"""
부분 회전?
- 2차원 배열의 특정 부분만 회전
"""
arr = [[7 * j + i for i in range(1, 8)] for j in range(7)]
sr, sc = 2, 2
length = 3

# 배열의 특정 부분(정사각형)을 회전시킨다
# (sr, sc) 좌표를 좌측 최상단 꼭지점으로 삼는 정사각형을 시계방향 90도 회전
def clock_90(sr, sc, length):
    new_arr = [row[:] for row in arr]
    n = len(arr)
    for r in range(sr, sr + length):
        for c in range(sc, sc + length):
            # 1단계: (0, 0) 으로 옮겨주는 변환을 진행
            o_r, o_c = r - sr, c - sc
            # 2단계: 90도 회전했을 떄의 좌표를 구함
            rotate_r, rotate_c = o_c, length - 1 - o_r
            # 3단계: 다시 (sr, sc)를 더해준다
            new_arr[sr + rotate_r][sc + rotate_c] = arr[r][c]
    return new_arr

def print_square(arr):
    for row in arr:
        print(row)
print('=' * 10, "초기 사각형", '=' * 10)
print_square(arr)
print('=' * 10, "{0}, {1} 에서 길이{2}인 정사각형을 90도 회전".format(sr, sc, length), '=' * 10)
print_square(clock_90(sr, sc, length))