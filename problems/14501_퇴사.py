n = int(input())
time = [0]
price = [0]
for _ in range(n):
    t, p = map(int, input().split())
    time.append(t)
    price.append(p)
time += [0] # dp 시행 시 n+1 까지 검사하기 위해 추가
price += [0] # dp 시행 시 n+1 까지 검사하기 위해 추가

# dp[i] = i일째에 얻을 수 있는 최대 이익
dp = [0] * (n+2)
for i in range(1, n+2):
    dp[i] = max(dp[i], dp[i-1])
    for j in range(i):
        if j + time[j] == i:
            dp[i] = max(dp[i], dp[j] + price[j])
print(dp[n+1])