from collections import deque

# n*n 크기의 땅
# m = 구매한 나무
# k년이 지난 후 살아남은 나무의 수를 출력한다
n, m, k = map(int, input().split())
ground = [[5] * (n) for _ in range(n)]
# 양분의 양
a = [list(map(int, input().split())) for _ in range(n)]
# 상도가 심은 나무의 정보
# 입력으로 주어지는 나무의 위치는 모두 서로 다름 
# (처음에는 나무 나이가 어린 순으로 정렬 신경 쓸 필요 없음)
trees = [[deque() for _ in range(n)] for __ in range(n)]
for _ in range(m):
    x, y, age = map(int, input().split())
    x -= 1; y -= 1
    trees[x][y].append(age)

def spring():
    after_spring = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            new_trees = deque()
            while trees[r][c]:
                # 자신의 나이만큼 양분을 먹고 나이가 1 증가
                tree_age = trees[r][c].popleft()
                if ground[r][c] >= tree_age:
                    ground[r][c] -= tree_age
                    new_trees.append(tree_age + 1)
                else:
                    # 여기서부터 양분을 못먹는 나무들
                    after_spring[r][c] += (tree_age // 2)
            # new_trees에 저장된 나무들을 다시 trees에 넣어준다
            trees[r][c] = new_trees
    return after_spring

def summer(after_spring):
    # 죽은 나무의 양분이 추가된다
    for r in range(n):
        for c in range(n):
            ground[r][c] += after_spring[r][c]

def fall():
    # 나무가 번식한다
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]

    baby_trees = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if not trees[r][c]:
                continue
            baby_tree_cnt = 0
            for i in range(len(trees[r][c])):
                # 나이가 5의 배수인 나무의 개수를 센다
                if trees[r][c][i] % 5 == 0:
                    baby_tree_cnt += 1
            # 주변 8구역에 baby_tree_cnt 개수만큼의 새 나무가 생긴다
            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < n and 0 <= nc < n:
                    baby_trees[nr][nc] += baby_tree_cnt
    # baby_trees와 trees를 합쳐준다
    for r in range(n):
        for c in range(n):
            if baby_trees[r][c] == 0:
                continue
            # baby_trees[r][c]의 개수만큼 1 나무 추가
            # appendleft로 해야 나무의 나이순으로 정렬된다
            for xxx in range(baby_trees[r][c]):
                trees[r][c].appendleft(1)

def winter():
    # 땅에 양분을 추가한다
    for r in range(n):
        for c in range(n):
            ground[r][c] += a[r][c]

def get_trees():
    # 남아있는 나무의 개수를 구한다
    ret = 0
    for r in range(n):
        for c in range(n):
            if trees[r][c]:
                ret += len(trees[r][c])
    return ret

while k > 0:
    after_spring = spring()
    summer(after_spring)
    fall()
    winter()
    k -= 1
    
print(get_trees())