# n = int(input())
# dp= [0] * ((10 ** n)+1)
# if n == 1:
# 	answer = 9
# else:
# 	for i in range((10**(n-1)),(10 ** n)):
# 		tmp = 0
# 		for j in range(len(str(i))):
# 			tmp = abs(int(str(i)[j])-tmp)
# 		if tmp == 1:
# 			# print(i)
# 			dp[i] +=1
# 	answer = sum(dp)

# print(answer % 1_000_000_000)


n = int(input())
dp = [[0] * 10 for _ in range(n+1)]

for i in range(1,10):
	dp[1][i] = 1

MAX = 1_000_000_000


for i in range(2,n+1):
	for j in range(10):
		if j == 0:
			dp[i][j] = dp[i-1][1]
		elif j == 9:
			dp[i][j] = dp[i-1][8]
		else:
			dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % MAX)
