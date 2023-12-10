import sys
input = sys.stdin.readline


t = int(input())
dp = [[0] * 31 for i in range(31)]

for i in range(31):
	for j in range(31):
		if i == 1:
			dp[i][j] = j
		else:
			if i == j:
				dp[i][j] = 1
			elif i < j:
				dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
# print(dp)

for i in range(t):
	n,m = map(int,input().split())
	print(dp[n][m])

# def factorial(n):
# 	num = 1
# 	for i in range(1, n+1):
# 		num *= i
# 	return num

# for i in range(t):
# 	n,m = map(int,input().split())
# 	print(factorial(m)// (factorial(m-n) * factorial(n)))



