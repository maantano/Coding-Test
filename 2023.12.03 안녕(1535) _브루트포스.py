


import sys
input = sys.stdin.readline

n = int(input())

minus = [0]+list(map(int,input().split()))
plus = [0]+list(map(int,input().split()))
dp = [[0] * 101 for _ in range(n+1)]

for i in range(1,n+1):
	for j in range(1,101):
		if minus[i] <= j:
			dp[i][j] = max(dp[i-1][j], dp[i-1][j- minus[i]]+ plus[i] )
		else:
			dp[i][j] = dp[i-1][j]
print(dp[n][99])


# if limit - z[0][0] <= 0:
# 	print(0)
# else:
# 	limit -= z[0][0]
# 	dp[0] = z[0][1]
# 	for i in range(1,n):
# 		limit -= z[i][0]
# 		for j in range(i+1,n):
# 			if limit - z[j][0] <0:
# 				continue
# 			else:
# 				limit -= z[j][0]
# 				dp[i] = max(dp[i],dp[j-1]+z[j][1])
# 				limit += z[j][0]

# 		limit += z[i][0]
# 	print(dp)

			# dp[i][0] = (dp[i-1][0] - dp[j][0]),








# import sys
# input = sys.stdin.readline

# n = int(input())

# minus = list(map(int,input().split()))
# plus = list(map(int,input().split()))

# answer = 0
# def dfs(limit,happy,idx):
# 	if idx == n:
# 		return happy
# 	else:
# 		limit -= minus[idx]
# 		happy+= plus[idx]
# 		if limit < 0:
# 			# print('happy =====>',happy)
# 			# print('plus[idx-1] =====>',plus[idx-1])
# 			# print('plus[idx] =====>',plus[idx])
# 			answer = happy-plus[idx]
# 			print('(happy-plus[idx]) ====>',(happy-plus[idx]))
# 			return answer
# 		dfs(limit,happy,idx+1)
# print(dfs(100,0,0))






