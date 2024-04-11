# 지도의 세로 크기 N, 가로 크기 M (1 ≤ N, M ≤ 20), 주사위를 놓은 곳의 좌표 x, y(0 ≤ x ≤ N-1, 0 ≤ y ≤ M-1), 그리고 명령의 개수 K (1 ≤ K ≤ 1,000)
n, m, r, c, k = map(int, input().split())
arr = [list(map(int ,input().split())) for _ in range(n)]
# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
cmds = list(map(int ,input().split()))
dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

def roll_east(dice):
    new_dice = [0] * 6
    new_dice[0] = dice[2]
    new_dice[1] = dice[0]
    new_dice[2] = dice[5]
    new_dice[3] = dice[3] # 고정
    new_dice[4] = dice[4] # 고정
    new_dice[5] = dice[1]
    return new_dice
def roll_west(dice):
    new_dice = [0] * 6
    new_dice[0] = dice[1]
    new_dice[1] = dice[5]
    new_dice[2] = dice[0]
    new_dice[3] = dice[3] # 고정
    new_dice[4] = dice[4] # 고정
    new_dice[5] = dice[2]
    return new_dice
def roll_south(dice):
    new_dice = [0] * 6
    new_dice[0] = dice[4]
    new_dice[1] = dice[1] # 고정
    new_dice[2] = dice[2] # 고정
    new_dice[3] = dice[0]
    new_dice[4] = dice[5]
    new_dice[5] = dice[3]
    return new_dice
def roll_north(dice):
    new_dice = [0] * 6
    new_dice[0] = dice[3]
    new_dice[1] = dice[1] # 고정
    new_dice[2] = dice[2] # 고정
    new_dice[3] = dice[5]
    new_dice[4] = dice[0]
    new_dice[5] = dice[4]
    return new_dice

# dice = [윗면, 윗면을 기준으로 동, 서, 남, 북, 아랫면]
dice = [0, 0, 0, 0, 0, 0]

for cmd in cmds:
    nr = r + dr[cmd]
    nc = c + dc[cmd]
    if 0 <= nr < n and 0 <= nc < m:
      if cmd == 1: #동
          dice = roll_east(dice)
      elif cmd == 2: # 서
          dice = roll_west(dice)
      elif cmd == 3: # 남
          dice = roll_south(dice)
      else: # 븍
          dice = roll_north(dice)
      
      if arr[nr][nc] == 0:
          arr[nr][nc] = dice[-1]
      else:
          dice[-1] = arr[nr][nc]
          arr[nr][nc] = 0
      # update
      r = nr
      c = nc
      print(dice[0])
