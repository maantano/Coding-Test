# 시간 초과

# import sys
# input = sys.stdin.readline
# import copy
# from collections import deque

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# INF = int(1e9)
# def bfs(x,y,arr):
# 	visited = [[0] * m for _ in range(n)]

# 	tmp = copy.deepcopy(arr)
# 	tmp[x][y] = 0

# 	q = deque([(0,0)])
# 	visited[0][0] = 1

# 	while q:
# 		x,y = q.popleft()

# 		for i in range(4):
# 			nx = x + dx[i]
# 			ny = y + dy[i]

# 			if 0 <= nx < n and 0<= ny < m and tmp[nx][ny] == 0:
# 				if not visited[nx][ny]:
# 					# visited[nx][ny] = 1
# 					visited[nx][ny] = visited[x][y] + 1
# 					q.append((nx,ny))
# 	if visited[n-1][m-1] == 0:
# 		visited[n-1][m-1] = INF
# 	return visited[n-1][m-1]

# n,m = map(int,input().split())
# arr = [list(map(int,input().rstrip())) for _ in range(n)]
# ans = INF

# for i in range(n):
# 	for j in range(m):
# 		if arr[i][j] == 1:
# 			ans = min(bfs(i,j,arr),ans)

# if ans == INF:
# 	print(-1)
# else:
# 	print(ans)




from collections import deque

n,m = map(int,input().split())

# 3차원 리스트(행,열,벽을 깬 여부)
graph = [list(map(int,input())) for _ in range(n)]

visited = [[[0]*2  for _ in range(m)] for _ in range(n)]

# [
# 	[
# 		[0, 0],
# 		[0, 0],
# 		[0, 0],
# 		[0, 0]
# 	],
# 	[
# 		[0, 0],
# 		[0, 0],
# 		[0, 0],
# 		[0, 0]
# 	],
# 	[
# 		[0, 0],
# 		[0, 0],
# 		[0, 0],
# 		[0, 0]
# 	],
# 	[
# 		[0, 0],
# 		[0, 0],
# 		[0, 0],
# 		[0, 0]
# 	],
# 	[
# 		[0, 0],
# 		[0, 0],
# 		[0, 0],
# 		[0, 0]
# 	],
# 	[
# 		[0, 0],
# 		[0, 0],
# 		[0, 0],
# 		[0, 0]
# 	]
# ]

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def solve(x,y,wall_break_left,visited,graph):
	q = deque()
	q.append((x,y,wall_break_left))
	visited[x][y][wall_break_left] = 1
	while q:
		x,y,wall_break_left = q.popleft()
		#  목적지 위치 도착
		if x == n-1 and y == m-1:
			# 최단 거리 횟수 리턴
			return visited[x][y][wall_break_left]
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			# 맵을 벗어나면 건너뛰기
			if nx <0 or nx >=n or ny <0 or ny >=m:
				continue
			# 벽을 부수지 않고 이동
			if graph[nx][ny] == 0 and visited[nx][ny][wall_break_left] == 0:
				q.append((nx,ny,wall_break_left))
				visited[nx][ny][wall_break_left] =  visited[x][y][wall_break_left] + 1
			# 벽을 부수고 이동
			if graph[nx][ny] == 1 and wall_break_left == 1:
				q.append((nx,ny,wall_break_left-1))
				visited[nx][ny][wall_break_left-1] = visited[x][y][wall_break_left] +1
	# 불가능할 경우 -1 리턴
	return -1

print(solve(0,0,1,visited,graph))
