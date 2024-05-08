dice = list(map(int, input().split()))

graph = [[] for _ in range(33)]
for i in range(20):
    graph[i].append(i+1)
graph[20].append(21)

graph[5].append(22)
graph[22].append(23)
graph[23].append(24)
graph[24].append(25)

graph[10].append(26)
graph[26].append(27)
graph[27].append(25)

graph[15].append(28)
graph[28].append(29)
graph[29].append(30)
graph[30].append(25)

graph[25].append(31)
graph[31].append(32)
graph[32].append(20)

score = [0] * 33
for i in range(21):
    score[i] = i * 2
score[22] = 13; score[23] = 16; score[24] = 19
score[25] = 25
score[26] = 22; score[27] = 24
score[28] = 28; score[29] = 27; score[30] = 26
score[31] = 30; score[32] = 35

answer = 0
meeples = [0, 0, 0, 0]

def dfs(meeples, idx, tmp):
    if idx == 10:
        global answer
        if answer < tmp:
            answer = tmp
        return
    
    for i in range(4):
        if meeples[i] == 21: # 도착 지점에 있는 노드
            continue

        node = meeples[i]

        original_node = node
        
        cnt = dice[idx] # 움직여야하는 횟수
        
        # 5, 10, 15번 인덱스에 위치해있는지 확인
        if node in (5, 10, 15):
            if node == 5:
                node = 22
            elif node == 10:
                node = 26
            else:
                node = 28
            cnt -= 1 # 움직임 횟수 1 줄여준다
        
        while cnt > 0:
            if node == 21:
                break # 도착
            node = graph[node][0]
            cnt -= 1
        
        # 도착지점 or 도착지점이 아니고, 다른 말이 없다면
        if node == 21 or (node != 21 and node not in meeples):
            meeples[i] = node
            dfs(meeples, idx + 1, tmp + score[node])
            # backtracking
            meeples[i] = original_node

dfs(meeples, 0, 0)
print(answer)