n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# 치킨집 중 m개만 살리고 나머지는 모두 폐업
# 어떻게 해야 도시의 치킨 거리가 가장 작게 되는가?

# 치킨집 좌표
chickens = []
# 집의 좌표
houses = []
for r in range(n):
    for c in range(n):
        if arr[r][c] == 2:
            chickens.append((r, c))
        elif arr[r][c] == 1:
            houses.append((r, c))

# 폐업시키지 않을 치킨 집을 m개 골라 조합을 만든다
combinations = []
def make_combinations(idx, tmp):
    if len(tmp) == m:
        global combinations
        combinations.append(tmp)
        return
    
    for i in range(idx, len(chickens)):
        make_combinations(i+1, tmp + [chickens[i]])
make_combinations(0, [])


# 만들어진 조합별로 도시의 치킨 거리 최솟값을 구한다
INF = float('inf')
answer = INF
for combi in combinations:
    city_chicken_dist = 0
    for r, c in houses:
        chicken_dist = INF
        if arr[r][c] == 1:
            chicken_dist = INF
            # 치킨 거리를 구한다
            for x, y in combi:
                chicken_dist = min(chicken_dist, abs(x - r) + abs(y - c))
            city_chicken_dist += chicken_dist
    answer = min(city_chicken_dist, answer)
print(answer)