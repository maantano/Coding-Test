import sys
input = sys.stdin.readline


d,k = map(int,input().split())
dp= [0] * (d)
dp[0],dp[1] = 1,1
while True:
	for i in range(2,d):
		dp[i] = dp[i-1] + dp[i-2]
	if dp[d-1] == k:
		print(dp[0],dp[1],sep='\n')
		break
	elif dp[-1] > k:
		dp[0] += 1
		dp[1] = dp[0]
	else:
		dp[1] += 1



# import sys

# d, k = map(int, sys.stdin.readline().split())
# for i in range(1, 100000):
# 	for j in range(1, 100000):
# 		dp = [0] * (d + 1)
# 		dp[1] = i
# 		dp[2] = j
# 		for l in range(3, d + 1):
# 			dp[l] = dp[l - 1] + dp[l - 2]
# 		if dp[-1] == k:
# 			print(dp[1])
# 			print(dp[2])
# 			exit()
