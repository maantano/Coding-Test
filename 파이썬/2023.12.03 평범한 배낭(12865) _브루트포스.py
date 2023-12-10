
import sys
input = sys.stdin.readline


n,k = map(int,input().split())

wl = [0]
vl = [0]
for i in range(n):
	w,v = map(int,input().split())
	wl.append(w)
	vl.append(v)
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1,n+1):
	for j in range(1,k+1):
		if j < wl[i]:
			dp[i][j] = dp[i-1][j]
		else:
			dp[i][j] = max(dp[i-1][j],dp[i-1][j-wl[i]]+vl[i])

print(dp[n][k])



# import sys
# input = sys.stdin.readline

# n = int(input())

# minus = [0]+list(map(int,input().split()))
# plus = [0]+list(map(int,input().split()))
# dp = [[0] * 101 for _ in range(n+1)]

# for i in range(1,n+1):
# 	for j in range(1,101):
# 		if minus[i] <= j:
# 			dp[i][j] = max(dp[i-1][j], dp[i-1][j- minus[i]]+ plus[i] )
# 		else:
# 			dp[i][j] = dp[i-1][j]
# print(dp[n][99])

