from collections import deque
# n: 세로선의 개수, m: 가로선의 개수, h: 세로선마다 가로선을 놓을 수 있는 위치의 개수
n, m, h = map(int, input().split())

arr = [[False] * (n+1) for _ in range(h + 1)]

# arr[a][b] = True -> arr[a][b], arr[a][b+1] 사이에 사다리
for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = True

# i번 세로선의 결과가 i번이 나오는지 체크하는 함수
def check():
    for dest in range(1, n+1):
        col = dest
        for row in range(1, h+1):
            if arr[row][col]:
                col += 1
            elif 0 <= col - 1 and arr[row][col-1]:
                col -= 1
        if col != dest:
            return False
    return True

# 사다리를 만든다
answer = float('inf')
def make_ladder(cnt, r, c):
    global answer
    
    if check():
        answer = min(answer, cnt)
        return
    
    if cnt == 3 or answer < cnt:
        # cnt가 3이면 다음에는 4를 검사해야하므로 중단
        # answer < cnt이면 현재 탐색하는 값은 최소값이 아니므로 중단
        return
    
    for i in range(r, h+1):
        if i == r:
            # 행이 변경되기 전에는 c열에서부터 탐색한다
            col = c
        else:
            # 행이 변경되었다면 1열에서부터 탐색한다
            col = 1

        for j in range(col, n):
            if not arr[i][j]:
                # 가로선을 긋고, 연속된 가로선을 긋지 않기 위해 j+2를 호출한다
                arr[i][j] = True
                make_ladder(cnt + 1, i, j+2) # cnt는 1 증가, 세로선은 2 증가
                arr[i][j] = False
            
make_ladder(0, 1, 1)
if answer == float('inf'):
    print(-1)
else:
    print(answer)