# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# arr = [list(map(int,input().rstrip())) for _ in range(m)]

# visited = [[-1] * n for _ in range(m)]
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# from collections import deque

# def bfs():
# 	q = deque([(0,0)])
# 	visited[0][0] = 0
# 	while q:
# 		x,y = q.popleft()

# 		for i in range(4):
# 			nx = x + dx[i]
# 			ny = y + dy[i]
# 			if nx < 0 or nx >= m or ny < 0 or ny >= n:
# 				continue
# 			# if 0<= nx < n and 0<= ny < m:
# 			if visited[nx][ny] == -1:
# 				if arr[nx][ny] == 0:
# 					visited[nx][ny] = visited[x][y]
# 					q.appendleft((nx,ny))
# 				else:
# 					arr[nx][ny] = 0
# 					visited[nx][ny] = visited[x][y]+1
# 					q.append((nx,ny))
# bfs()
# print(visited[m-1][n-1])

import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr = [list(map(int,input().rstrip())) for _ in range(m)]
INF = int(1e9)
distance = [[INF] * n for _ in range(m)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]


import heapq
def djikstra():
	q = []
	heapq.heappush(q,(0,0,0))
	distance[0][0] = 0

	while q:
		dist,r,c = heapq.heappop(q)
		if distance[r][c] < dist:
			continue
		for i in range(4):
			nr = r + dx[i]
			nc = c + dy[i]

			if nr < 0 or nr >= m or nc < 0 or nc >=n:
				continue

			if dist+arr[nr][nc] < distance[nr][nc]:
				distance[nr][nc] = dist+arr[nr][nc]
				heapq.heappush(q,(distance[nr][nc],nr,nc))

djikstra()
print(distance[m-1][n-1])





