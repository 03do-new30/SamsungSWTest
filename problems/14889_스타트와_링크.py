n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

arr = [x for x in range(1, n+1)]
all_combinations = []
def combinations(goal, current, index):
    if len(current) == goal:
        all_combinations.append(current)
    for i in range(index + 1, n+1):
        combinations(goal, current + [i], i)
combinations(n//2, [], 0)

min_diff = float('inf')
for i in range(len(all_combinations) // 2):
    team1 = all_combinations[i]
    team2 = [x for x in range(1, n+1) if x not in team1]
    
    stat1 = 0
    for a in team1:
        for b in team1:
            if a == b:
                continue
            stat1 += s[a-1][b-1]
    stat2 = 0
    for a in team2:
        for b in team2:
            if a == b:
                continue
            stat2 += s[a-1][b-1]
    
    tmp = abs(stat1 - stat2)
    if tmp < min_diff:
        # print("team1:", team1, "team2:", team2)
        min_diff = tmp

print(min_diff)