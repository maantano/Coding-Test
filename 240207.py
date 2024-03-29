# 평범한 배낭
# https://www.acmicpc.net/problem/12865



# import sys
# input = sys.stdin.readline

# n,k = map(int,input().split())
# arr = [[0,0]]+[list(map(int,input().split())) for _ in range(n)]
# dp =[[0 for _ in range(k+1)] for _ in range(n+1)]

# for i in range(1,n+1):
# 	w,v = arr[i]
# 	for j in range(1,k+1):
# 		if  j < w:
# 			dp[i][j] = dp[i-1][j]
# 		else:
# 			dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])

# print(dp[n][k])


# 구간 합 구하기 5
# https://www.acmicpc.net/problem/11660

# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# arr = []
# for i in range(n):
# 	a = list(map(int, input().split()))
# 	arr.append(a)

# dp = [[0]*(n+1) for i in range(n+1)]

# for i in range(1, n+1):
# 	for j in range(1, n+1):
# 		dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i-1][j-1]

# for k in range(m):
# 	x1,y1,x2,y2 = map(int,input().split())

# 	result = dp[x2][y2] - dp[x2][y1-1] -dp[x1-1][y2] + dp[x1-1][y1-1]
# 	print(result)


# 동전 1
# https://www.acmicpc.net/problem/2293



n,k = map(int,input().split())
arr = sorted([int(input()) for _ in range(n)])

dp = [0] * (k+1)
dp[0] = 1

for c in arr:
	for i in range(c,k+1):
		dp[i] += dp[i-c]
print(dp[k])



