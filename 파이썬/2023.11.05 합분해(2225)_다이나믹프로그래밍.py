import sys
input = sys.stdin.readline

n,k= map(int,input().split())
dp = [[0] * (20) for _ in range(20)]
for i in range(20):
	dp[1][i] = 1
	dp[2][i] = i+1

for i in range(2,20):
	dp[i][1] = i
	for j in range(2,20):
		dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1_000_000_000

print(dp[k][n])




