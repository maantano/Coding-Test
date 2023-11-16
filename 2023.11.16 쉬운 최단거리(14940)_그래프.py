import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

g = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
	q = deque([(x,y)])
	visited[x][y] = 0

	while q:
		x,y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < n and 0<= ny < m:
				# for i in range(1,n+1):
				if visited[nx][ny] == -1 and g[nx][ny]:
					visited[nx][ny] = visited[x][y] +1
					q.append((nx,ny))
				if visited[nx][ny] == -1 and not g[nx][ny]:
					visited[nx][ny] = 0



for i in range(n):
	for j in range(m):
		if g[i][j] == 2 :
			bfs(i,j)

for i in range(n):
	for j in range(m):
		if not g[i][j]:
			print(0, end =' ')
		else:
			print(visited[i][j],end=' ')
	print()


# import sys
# input = sys.stdin.readline

# from collections import deque
# N, M = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(N)]
# visited = [[-1] * M for _ in range(N)]
# dx, dy = [0,0,-1,1], [-1,1,0,0]

# def bfs(i,j):
# 	queue = deque()
# 	queue.append((i,j))

# 	visited[i][j] = 0

# 	while queue:
# 		x, y = queue.popleft()

# 		for i in range(4):
# 			nx, ny = dx[i] + x, dy[i] + y

# 			if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
# 				if graph[nx][ny] == 0:
# 					visited[nx][ny] = 0
# 				elif graph[nx][ny] == 1:
# 					visited[nx][ny] = visited[x][y] + 1
# 					queue.append((nx,ny))

# for i in range(N):
# 	for j in range(M):
# 		if graph[i][j] == 2 and visited[i][j] == -1:
# 			bfs(i,j)

# for i in range(N):
# 	for j in range(M):
# 		if graph[i][j] == 0:
# 			print(0, end=' ')
# 		else:
# 			print(visited[i][j], end=' ')
# 	print()
