n = int(input())

arr = [[0] * n for _ in range(n)]
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def in_boundary(r, c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False

# 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다
def step1(arr, friends):
    max_cnt = 0 # 인접한 칸에 있는 좋아하는 학생 수
    candidates = [] # 1을 만족하는 칸
    for r in range(n):
        for c in range(n):
            if arr[r][c] == 0:
                cnt = 0
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if not in_boundary(nr, nc):
                        continue
                    if arr[nr][nc] in friends:
                        cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
                    candidates = [(r, c)]
                elif cnt == max_cnt:
                    candidates.append((r, c))
    return candidates

def step2(arr, candidates):
    max_cnt = 0 # 인접한 칸에 있는 비어있는 칸 수
    step2_candidates = []
    for r, c in candidates:
        cnt = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not in_boundary(nr, nc):
                continue
            if arr[nr][nc] == 0:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            step2_candidates = [(r, c)]
        elif cnt == max_cnt:
            step2_candidates.append((r, c))
    return step2_candidates

def step3(candidates):
    # 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러개이면 열의 번호가 가장 작은 칸으로
    candidates.sort(key = lambda x : (x[0], x[1]))
    return candidates[0]

def get_seat(arr, friends):
    # step1 
    candidates = step1(arr, friends)
    if len(candidates) == 1:
        return candidates[0]
    # step2
    candidates = step2(arr, candidates)
    if len(candidates) == 1:
        return candidates[0]
    # step3
    return step3(candidates)

friends_dict = dict()

for _ in range(n*n):
    student, s1, s2, s3, s4 = map(int, input().split())
    friends = [s1, s2, s3, s4]
    friends_dict[student] = friends
    seat = get_seat(arr, friends)
    arr[seat[0]][seat[1]] = student

# 만족도 계산
answer = 0
for r in range(n):
    for c in range(n):
        id = arr[r][c]
        cnt = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not in_boundary(nr, nc):
                continue
            if arr[nr][nc] in friends_dict[id]:
                cnt += 1
        if cnt > 0:
            answer += 10**(cnt-1)
print(answer)