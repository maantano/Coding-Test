n,m = map(int,input().split())

arr1 = [list(map(int,input().split())) for _ in range(n)]
m,k = map(int,input().split())
arr2 = [list(map(int,input().split())) for _ in range(m)]

dp = [[0] * k for _ in range(n)]

for r in range(n):
	for c in range(k):
		e = 0
		for i in range(m):
			e += arr1[r][i] * arr2[i][c]
		dp[r][c] = e
for r in dp:
	print(*r)
