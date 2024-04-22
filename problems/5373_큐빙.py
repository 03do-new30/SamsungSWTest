from collections import deque

up = [['w'] * 3 for _ in range(3)]
down = [['y'] * 3 for _ in range(3)]
front = [['r'] * 3 for _ in range(3)]
back = [['o'] * 3 for _ in range(3)]
left = [['g'] * 3 for _ in range(3)]
right = [['b'] * 3 for _ in range(3)]


def initialize_cube():
    global up, down, front, back, left, right
    up = [['w'] * 3 for _ in range(3)]
    down = [['y'] * 3 for _ in range(3)]
    front = [['r'] * 3 for _ in range(3)]
    back = [['o'] * 3 for _ in range(3)]
    left = [['g'] * 3 for _ in range(3)]
    right = [['b'] * 3 for _ in range(3)]

def debug_cube():
    print("up", '!' * 20)
    for row in up:
        print(row)
    print("left", '!' * 20)
    for row in left:
        print(row)
    print("front", '!' * 20)
    for row in front:
        print(row)
    print("right", '!' * 20)
    for row in right:
        print(row)
    print("back", '!' * 20)
    for row in back:
        print(row)
    print("down", '!' * 20)
    for row in down:
        print(row)
    print('=' * 30)

def get_ith_col(arr3x3, i):
    ret = []
    for r in range(3):
        ret.append(arr3x3[r][i])
    return ret

def self_rotate(target, param):
    new_arr = [[''] * 3 for _ in range(3)]
    # 시계방향
    if param == 1:
        for r in range(3):
            for c in range(3):
                new_arr[c][2-r] = target[r][c]
    # 반시계방향
    else:
        for r in range(3):
            for c in range(3):
                new_arr[2-c][r] = target[r][c]
    for r in range(3):
        for c in range(3):
            target[r][c] = new_arr[r][c]

 
def up_rotate(param):
    self_rotate(up, param)

    tmp_front = front[0]
    tmp_right = right[0]
    tmp_back = back[0]
    tmp_left = left[0]
    
    if param == 1:
        front[0] = tmp_right
        right[0] = tmp_back
        back[0] = tmp_left
        left[0] = tmp_front
    else:
        front[0] = tmp_left
        right[0] = tmp_front
        back[0] = tmp_right
        left[0] = tmp_back

def down_rotate(param):
    global right, front, left, back

    self_rotate(down, param)

    new_right = [row[:] for row in right]
    new_front = [row[:] for row in front]
    new_left = [row[:] for row in left]
    new_back = [row[:] for row in back]

    if param == 1:
        new_front[2][2] = left[2][2]
        new_front[2][1] = left[2][1]
        new_front[2][0] = left[2][0]

        new_right[2][2] = front[2][2]
        new_right[2][1] = front[2][1]
        new_right[2][0] = front[2][0]

        new_left[2][2] = back[2][2]
        new_left[2][1] = back[2][1]
        new_left[2][0] = back[2][0]

        new_back[2][2] = right[2][2]
        new_back[2][1] = right[2][1]
        new_back[2][0] = right[2][0]
    else:
        new_front[2][2] = right[2][2]
        new_front[2][1] = right[2][1]
        new_front[2][0] = right[2][0]

        new_right[2][2] = back[2][2]
        new_right[2][1] = back[2][1]
        new_right[2][0] = back[2][0]

        new_left[2][2] = front[2][2]
        new_left[2][1] = front[2][1]
        new_left[2][0] = front[2][0]

        new_back[2][2] = left[2][2]
        new_back[2][1] = left[2][1]
        new_back[2][0] = left[2][0]
    front = new_front
    right = new_right
    left = new_left
    back = new_back

def front_rotate(param):
    global up, right, down, left

    self_rotate(front, param)
    new_up = [row[:] for row in up]
    new_left = [row[:] for row in left]
    new_right = [row[:] for row in right]
    new_down = [row[:] for row in down]
    if param == 1:
        new_up[2][0] = left[2][2] 
        new_up[2][1] = left[1][2]
        new_up[2][2] = left[0][2]

        new_right[0][0] = up[2][0] 
        new_right[1][0] = up[2][1]
        new_right[2][0] = up[2][2]

        new_down[2][2] = right[2][0] 
        new_down[2][1] = right[1][0]
        new_down[2][0] = right[0][0]

        new_left[0][2] = down[2][2]
        new_left[1][2] = down[2][1]
        new_left[2][2] = down[2][0]
    else:
        new_up[2][0] = right[0][0]
        new_up[2][1] = right[1][0]
        new_up[2][2] = right[2][0]

        new_right[0][0] = down[2][0]
        new_right[1][0] = down[2][1]
        new_right[2][0] = down[2][2]

        new_down[2][2] = left[0][2]
        new_down[2][1] = left[1][2]
        new_down[2][0] = left[2][2]

        new_left[0][2] = up[2][2]
        new_left[1][2] = up[2][1]
        new_left[2][2] = up[2][0]
    
    up = new_up
    right = new_right
    down = new_down
    left = new_left

def back_rotate(param):
    global up, right, down, left

    self_rotate(back, param)
    new_up = [row[:] for row in up]
    new_left = [row[:] for row in left]
    new_right = [row[:] for row in right]
    new_down = [row[:] for row in down]
    if param == 1:
        new_up[0][2] = right[2][2]
        new_up[0][1] = right[1][2]
        new_up[0][0] = right[0][2]

        new_right[0][2] = down[0][0]
        new_right[1][2] = down[0][1]
        new_right[2][2] = down[0][2]

        new_down[0][0] = left[2][0]
        new_down[0][1] = left[1][0]
        new_down[0][2] = left[0][0]

        new_left[0][0] = up[0][2]
        new_left[1][0] = up[0][1]
        new_left[2][0] = up[0][0]
    else:
        new_up[0][2] = left[0][0]
        new_up[0][1] = left[1][0]
        new_up[0][0] = left[2][0]

        new_right[0][2] = up[0][0]
        new_right[1][2] = up[0][1]
        new_right[2][2] = up[0][2]

        new_down[0][0] = right[0][2]
        new_down[0][1] = right[1][2]
        new_down[0][2] = right[2][2]

        new_left[0][0] = down[0][2]
        new_left[1][0] = down[0][1]
        new_left[2][0] = down[0][0]
    
    up = new_up
    right = new_right
    down = new_down
    left = new_left

def left_rotate(param):
    global up, back, front, down

    self_rotate(left, param)
    new_up = [row[:] for row in up]
    new_back = [row[:] for row in back]
    new_front = [row[:] for row in front]
    new_down = [row[:] for row in down]
    if param == 1:
        new_up[0][0] = back[2][2]
        new_up[1][0] = back[1][2]
        new_up[2][0] = back[0][2]

        new_back[0][2] = down[0][2]
        new_back[1][2] = down[1][2]
        new_back[2][2] = down[2][2]

        new_front[0][0] = up[0][0]
        new_front[1][0] = up[1][0]
        new_front[2][0] = up[2][0]
        
        new_down[0][2] = front[2][0]
        new_down[1][2] = front[1][0]
        new_down[2][2] = front[0][0]
    else:
        new_up[0][0] = front[0][0]
        new_up[1][0] = front[1][0]
        new_up[2][0] = front[2][0]

        new_back[0][2] = up[2][0]
        new_back[1][2] = up[1][0]
        new_back[2][2] = up[0][0]

        new_front[0][0] = down[2][2]
        new_front[1][0] = down[1][2]
        new_front[2][0] = down[0][2]
        
        new_down[0][2] = back[0][2]
        new_down[1][2] = back[1][2]
        new_down[2][2] = back[2][2]
    
    up = new_up
    back = new_back
    front = new_front
    down = new_down

def right_rotate(param):
    global up, back, front, down

    self_rotate(right, param)
    new_up = [row[:] for row in up]
    new_back = [row[:] for row in back]
    new_front = [row[:] for row in front]
    new_down = [row[:] for row in down]
    if param == 1:
        new_up[2][2] = front[2][2]
        new_up[1][2] = front[1][2]
        new_up[0][2] = front[0][2]

        new_back[0][0] = up[2][2]
        new_back[1][0] = up[1][2]
        new_back[2][0] = up[0][2]

        new_front[0][2] = down[2][0]
        new_front[1][2] = down[1][0]
        new_front[2][2] = down[0][0]

        new_down[2][0] = back[2][0]
        new_down[1][0] = back[1][0]
        new_down[0][0] = back[0][0]
    else:
        new_up[2][2] = back[0][0]
        new_up[1][2] = back[1][0]
        new_up[0][2] = back[2][0]

        new_back[0][0] = down[0][0]
        new_back[1][0] = down[1][0]
        new_back[2][0] = down[2][0]

        new_front[0][2] = up[0][2]
        new_front[1][2] = up[1][2]
        new_front[2][2] = up[2][2]

        new_down[2][0] = front[0][2]
        new_down[1][0] = front[1][2]
        new_down[0][0] = front[2][2]
    
    up = new_up
    back = new_back
    front = new_front
    down = new_down

    
# test
# right_rotate(-1)
# debug_cube()


testcases = int(input())
for tc in range(testcases):
    # 큐브 초기화
    initialize_cube()
    cmd_size = int(input())
    cmds = input().split()
    for cmd in cmds:
        side = cmd[0]
        param = cmd[1]
        # if param == '+':
        #     param = 1
        # else:
        #     param = -1
        if side == 'U':
            if param == '+':
                param = 1
                up_rotate(param)
            else:
                # 반시계는 시계를 3번
                # (디버깅 시계방향 반시계방향 각각 해주기 너무 귀찮아서 일단 시계방향 3번 돌리는걸로 반시계 대체)
                up_rotate(1)
                up_rotate(1)
                up_rotate(1)

        elif side == 'D':
            if param == '+':
                param = 1
                down_rotate(param)
            else:
                down_rotate(1)
                down_rotate(1)
                down_rotate(1)

        elif side == 'F':
            if param == '+':
                param = 1
                front_rotate(param)
            else:
                front_rotate(1)
                front_rotate(1)
                front_rotate(1)

        elif side == 'B':
            if param == '+':
                param = 1
                back_rotate(param)
            else:
                back_rotate(1)
                back_rotate(1)
                back_rotate(1)

        elif side == 'L':
            if param == '+':
                param = 1
                left_rotate(param)
            else:
                left_rotate(1)
                left_rotate(1)
                left_rotate(1)

        else:
            if param == '+':
                param = 1
                right_rotate(param)
            else:
                right_rotate(1)
                right_rotate(1)
                right_rotate(1)

        # print("let's debug for cmd:", cmd)
        # debug_cube()
    # 출력 (뒷면과 접하는 칸부터 출력한다)
    for row in up:
        print(''.join(row))
    # print('#' * 30)
