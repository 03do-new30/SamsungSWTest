n = int(input())
a = list(map(int, input().split()))
# +, -, x, /
operators = list(map(int, input().split()))

max_val = -float('inf')
min_val = float('inf')

def solve(result, idx):
    global max_val, min_val
    if idx == n-1:
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return
    
    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            if i == 0: # +
                solve(result + a[idx+1], idx + 1)
            elif i == 1: # -
                solve(result - a[idx+1], idx + 1)
            elif i == 2: # x
                solve(result * a[idx+1], idx + 1)
            else: # /
                if result < 0:
                    solve(-((-result) // a[idx+1]), idx + 1)
                else:
                    solve(result // a[idx+1], idx + 1)
            operators[i] += 1

solve(a[0], 0)
print(max_val)
print(min_val)