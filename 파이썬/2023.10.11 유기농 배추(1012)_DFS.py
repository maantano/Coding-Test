dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dfs(x,y):
	if x < 0 or x >= n or y < 0 or y >= m:
		return False
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if (0 <= nx < n) and (0 <= ny < m):
			if g[nx][ny] == 1:
				g[nx][ny] = 0
				dfs(nx,ny)
	return True




import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
T = int(input())

for i in range(T):
	bugs= 0
	m,n,k = map(int,input().split())
	g = [[0]*m for _ in range(n)]
	for i in range(k):
		a,b = map(int,input().split())
		g[b][a] = 1
	result = 0
	for i in range(n):
		for j in range(m):
			if g[i][j] == 1:
				result += dfs(i,j)
	print(result)






# import sys
# sys.setrecursionlimit(10000)

# def dfs(x, y):
# 	dx = [1, -1, 0, 0]
# 	dy = [0, 0, 1, -1]

# 	for i in range(4):
# 		nx = x + dx[i]
# 		ny = y + dy[i]
# 		if (0 <= nx < N) and (0 <= ny < M):
# 			if matrix[nx][ny] == 1:
# 				matrix[nx][ny] = -1
# 				dfs(nx, ny)

# T = int(input())
# for _ in range(T):
# 	M, N, K = map(int, input().split())
# 	matrix = [[0]*M for _ in range(N)]
# 	cnt = 0

# 	for _ in range(K):
# 		m, n = map(int, input().split())
# 		matrix[n][m] = 1

# 	for i in range(N): # 행 (바깥 리스트)
# 		for j in range(M): # 열 (내부 리스트)
# 			if matrix[i][j] > 0:
# 				dfs(i, j)
# 				cnt += 1
# 				print(cnt)

