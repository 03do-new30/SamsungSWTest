target_r, target_c, k = map(int, input().split())
target_r -= 1
target_c -= 1
arr = [list(map(int, input().split()))for _ in range(3)]

def r_cmd(arr):
    n = len(arr); m = len(arr[0])
    new_arr = []
    for row in arr:
        nums = dict()
        for num in row:
            # 0은 정렬 시 무시한다
            if num == 0:
                continue
            if num in nums:
                nums[num] += 1
            else:
                nums[num] = 1
        tmp = sorted(nums.items(), key = lambda x : (x[1], x[0]))
        new_row = []
        for key, val in tmp:
            new_row.append(key)
            new_row.append(val)
        new_arr.append(new_row)
    # new_arr 길이 맞춰주기
    max_col_len = 0
    for i in range(n):
        if len(new_arr[i]) > max_col_len:
            max_col_len = len(new_arr[i])
    
    for i in range(n):
        while len(new_arr[i]) < max_col_len:
            new_arr[i].append(0)
    
    return new_arr

def c_cmd(arr):
    n = len(arr); m = len(arr[0])
    new_cols = []
    for c in range(m):
        nums = dict()
        for r in range(n):
            # 0은 정렬 시 무시한다
            if arr[r][c] == 0:
                continue
            if arr[r][c] in nums:
                nums[arr[r][c]] += 1
            else:
                nums[arr[r][c]] = 1
        tmp = sorted(nums.items(), key = lambda x : (x[1], x[0]))
        new_col = []
        for key, val in tmp:
            new_col.append(key)
            new_col.append(val)
        new_cols.append(new_col)
    # new_arr 길이 맞춰주기
    max_row_len = 0
    for c in range(m):
        if max_row_len < len(new_cols[c]):
            max_row_len = len(new_cols[c])
    
    new_arr = [[0] * m for _ in range(max_row_len)]
    for c in range(m):
        for r in range(len(new_cols[c])):
            new_arr[r][c] = new_cols[c][r]
    return new_arr

def solve(arr, cnt):
    n = len(arr); m = len(arr[0])

    if target_r < n and target_c < m:
        if arr[target_r][target_c] == k:
            return cnt
    if cnt >= 100:
        return -1
    
    if n >= m:
        return solve(r_cmd(arr), cnt + 1)
    else:
        return solve(c_cmd(arr), cnt + 1)
    
answer = solve(arr, 0)
print(answer)