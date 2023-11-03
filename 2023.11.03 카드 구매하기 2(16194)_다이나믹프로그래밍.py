# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = [0] + list(map(int,input().split(' ')))
# dp = [False] * (n+1)

# # dp[1] = arr[1]

# for i in range(1,n+1):
# 	for j in range(1,i+1):
# 		if dp[i] == False:
# 			dp[i] = dp[i-j] + arr[j]
# 		else:
# 			dp[i] = min(dp[i],dp[i-j]+arr[j])

# print(dp[n])


import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int,input().split(' ')))
INF = int(1e9)
dp = [INF] * (n+1)
dp[0] = 0
# dp[1] = arr[1]

for i in range(1,n+1):
	for j in range(1,i+1):
		dp[i] = min(dp[i],dp[i-j]+arr[j])

print(dp[n])
