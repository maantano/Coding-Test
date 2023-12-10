import sys
input = sys.stdin.readline
n = int(input())

g = [list(map(int,input().split())) for i in range(n)]

dp = [0 for i in range(n+1)]

for i in range(n):
	for j in range(i+g[i][0],n+1):
		print(dp)
		if dp[j] < dp[i] + g[i][1]:
			dp[j] = dp[i] + g[i][1]

print(dp[-1])

