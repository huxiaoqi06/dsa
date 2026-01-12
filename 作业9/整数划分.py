MAX_N = 50
dp = [[0] * (MAX_N + 1) for _ in range(MAX_N + 1)]

for j in range(MAX_N + 1):
    dp[0][j] = 1

for i in range(1, MAX_N + 1):
    for j in range(1, MAX_N + 1):
        if j > i:
            dp[i][j] = dp[i][i]
        elif j == i:
            dp[i][j] = dp[i][j-1] + 1
        else:
            dp[i][j] = dp[i-j][j] + dp[i][j-1]


try:
    while True:
        line = input().strip()
        if not line:
            break
        n = int(line)
        print(dp[n][n])
except EOFError:
    pass