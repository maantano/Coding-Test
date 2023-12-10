
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
# arr = [[0] * m]
# for i in range(n):
# 	arr.append(list(map(int,input().split(' '))))
arr = [list(map(int,input().split())) for _ in range(n)]

dp= [[0]*(m+1) for _ in range(n+1)]

for r in range(1,n+1):
	for c in range(1,m+1):
		dp[r][c] = arr[r-1][c-1] + dp[r][c-1] + dp[r-1][c] - dp[r-1][c-1]
		for i in range(n+1):
			print(dp[i],end='\n')
		print('--------------------------')
		# print(dp)
# [0, 0, 0, 0],
# [0, 1, 3, 7],
# [0, 9, 27, 63]

print(dp)

# k = int(input())
# for _ in range(k):
# 	x,y,i,j = map(int,input().split())
# 	print(dp[i][j] - dp[x-1][j] - dp[i][y-1] - dp[x-1][y-1],end='\n')


# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]

# K = int(input())
# dp = [[0] * (M+1) for _ in range(N+1)]

# for i in range(1, N+1):
# 	for j in range(1, M+1):
# 		dp[i][j] = arr[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

# for _ in range(K):
# 	i, j, x, y = map(int, input().split())
# 	print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])
# # for i in range(n):
# # 	for j in range(m):





