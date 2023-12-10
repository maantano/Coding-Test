# import sys
# input = sys.stdin.readline
# INF = int(1e9)
# dp = [INF] * 16
# dp[0] = 4
# dp[1] = 9
# dp[2] = 25

# n = int(input())
# for i in range(3,16):
# 	# dp[i] = (dp[i-1] * 2)  + (dp[i-1] - ((i+1) * 2) * 2) - 1
# 	dp[i]= dp[i-1]+(2**(i-1))

# print(dp[n])


# # 25 + 25 +


import sys
input = sys.stdin.readline
dp = [0] * 16
dp[0] = 2


n = int(input())
for i in range(1,n+1):
	dp[i]= dp[i-1]+(2**(i-1))
print(dp[n]**2)


# 25 + 25 +
