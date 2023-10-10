# 플로이드 워셜 알고리즘

INF = int(1e9)

n,m = map(int,input().split())

g = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
	for j in range(1,n+1):
		if i == j:
			g[i][j] = 0

for _ in range(m):
	a,b = map(int,input().split())
	g[a][b] = 1
	g[b][a] = 1

x,k = map(int,input().split())

for k in range(1,n+1):
	for a in range(1,n+1):
		for b in range(1,n+1):
			g[a][b] = min(g[a][b],g[a][k]+g[k][b])

distance = g[1][k] + g[k][x]

if distance >= INF:
	print(-1)
else:
	print(distance)


# INPUT
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

# OUTPUT
# 3

# INPUT
# 4 2
# 1 3
# 2 4

# OUTPUT
# 3 4
