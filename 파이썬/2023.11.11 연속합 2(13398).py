import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

dp = [[x for x in arr] for _ in range(2)]
print(dp)
for i in range(1, n):
	dp[0][i] = max(dp[0][i - 1] + arr[i], dp[0][i])
	dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + arr[i])
print(dp)
# print(max(max(dp[0]), max(dp[1])))
# dp[0][0],dp[0][1] = arr[0],0

# for i in range(1,n):
# 	dp[i][1]= dp[i-1][0] + arr[i]
# 	dp[i][0]= dp[i-1][1] + arr[i]
# print(dp)
