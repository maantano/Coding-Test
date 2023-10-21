


import sys
input = sys.stdin.readline

from collections import deque

n,m = map(int,input().split())
g = [list(map(int,input().rstrip())) for i in range(n)]

visited = [[[0]*2 for _ in range(m)] for i in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,wall,visited,g):
	q = deque([(x,y,wall)])
	visited[x][y][wall] = 1
	while q:
		x,y,wall = q.popleft()

		if x == n-1 and y == m-1:
			return visited[x][y][wall]

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if  nx < 0 or nx >= n or 0 > ny or ny >= m:
				continue
			if  g[nx][ny] == 0 and not visited[nx][ny][wall]:
				q.append((nx,ny,wall))
				visited[nx][ny][wall] = visited[x][y][wall]+1

			if g[nx][ny] == 1 and wall == 1:
				visited[nx][ny][wall-1] = visited[x][y][wall] + 1
				q.append((nx,ny,wall-1))
	return -1



print(bfs(0,0,1,visited,g))





# from collections import deque
# n,m = map(int,input().split())
# # 3차원 리스트(행,열,벽을 깬 여부)
# graph = [list(map(int,input())) for _ in range(n)]

# visited = [[[0]*2  for _ in range(m)] for _ in range(n)]

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]


# def solve(x,y,wall_break_left,visited,graph):
# 	q = deque()
# 	q.append((x,y,wall_break_left))
# 	visited[x][y][wall_break_left] = 1
# 	while q:
# 		x,y,wall_break_left = q.popleft()
# 		#  목적지 위치 도착
# 		if x == n-1 and y == m-1:
# 			# 최단 거리 횟수 리턴
# 			return visited[x][y][wall_break_left]
# 		for i in range(4):
# 			nx = x + dx[i]
# 			ny = y + dy[i]
# 			# 맵을 벗어나면 건너뛰기
# 			if nx <0 or nx >=n or ny <0 or ny >=m:
# 				continue
# 			# 벽을 부수지 않고 이동
# 			if graph[nx][ny] == 0 and visited[nx][ny][wall_break_left] == 0:
# 				q.append((nx,ny,wall_break_left))
# 				visited[nx][ny][wall_break_left] =  visited[x][y][wall_break_left] + 1
# 			# 벽을 부수고 이동
# 			if graph[nx][ny] == 1 and wall_break_left == 1:
# 				q.append((nx,ny,wall_break_left-1))
# 				visited[nx][ny][wall_break_left-1] = visited[x][y][wall_break_left] +1
# 	# 불가능할 경우 -1 리턴
# 	return -1

# print(solve(0,0,1,visited,graph))
