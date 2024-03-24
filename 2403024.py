
# 인구인동
# https://www.acmicpc.net/problem/16234

# from collections import deque
# import sys
# input = sys.stdin.readline


# n,l,r = map(int,input().split())
# g = [list(map(int,input().split())) for _ in range(n)]
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def bfs(x,y):
# 	q = deque([(x,y)])
# 	arr = []
# 	arr.append((x,y))

# 	while q:
# 		x,y = q.popleft()
# 		for i in range(4):
# 			nx = dx[i] +  x
# 			ny = dy[i] +  y

# 			if 0<= nx < n and 0<= ny < n:
# 				if not visited[nx][ny]:
# 					if l <= abs(g[x][y] - g[nx][ny])<=r:
# 						arr.append((nx,ny))
# 						visited[nx][ny] = 1
# 						q.append((nx,ny))
# 	if len(arr) <= 1:
# 		return 0
# 	result = sum(g[a][b] for a,b in arr) // len(arr)
# 	for a,b in arr:
# 		g[a][b] = result
# 	return 1


# day = 0

# while True:
# 	stop = 0
# 	visited = [[0]*n for _ in range(n)]
# 	for i in range(n):
# 		for j in range(n):
# 			if not visited[i][j]:
# 				visited[i][j] = 1
# 				stop+=bfs(i,j)
# 	if not stop:
# 		break
# 	day+=1
# print(day)


# 이분 그래프
# https://www.acmicpc.net/problem/1707

# import sys
# input = sys.stdin.readline
# from collections import deque

# def sol():
# 	for _ in range(k):
# 		V,E = map(int,input().split())
# 		g = [[] for _ in range(V+1)]
# 		for i in range(E):
# 			u,v = map(int,input().split())
# 			g[u].append(v)
# 			g[v].append(u)

# 		visited = [0] * (V+1)

# 		for i in range(1,V+1):
# 			if visited[i]:
# 				continue
# 			visited[i] = 1

# 			q = deque([i])
# 			while q:
# 				now = q.popleft()
# 				nextVisited = visited[now] % 2 +1

# 				for next in g[now]:
# 					if not visited[next]:
# 						visited[next] = nextVisited
# 						q.append(next)
# 					elif visited[next] != nextVisited:
# 						return 'NO'
# 		return 'YES'


# k = int(input())
# for _ in range(k):
# 	print(sol())


# 토마토
# https://www.acmicpc.net/problem/7569

# import sys
# input = sys.stdin.readline

# from collections import deque

# m,n,h = map(int,input().split())
# g = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
# visited = [[[0]*m for _ in range(n)] for _ in range(h)]
# q = deque()
# dy = [-1,1,0,0,0,0]
# dx = [0,0,-1,1,0,0]
# dz = [0,0,0,0,-1,1]

# def bfs():
# 	while q:
# 		z,x,y= q.popleft()

# 		for i in range(6):
# 			nx = dx[i] + x
# 			ny = dy[i] + y
# 			nz = dz[i] + z

# 		if 0<=nz<h and 0<=nx <n and 0<= ny < m:
# 			if not visited[nz][nx][ny]:
# 				if g[nz][nx][ny] == 0:
# 					q.append((nz,nx,ny))
# 					g[nz][nx][ny] = g[z][x][y] + 1
# 					visited[nz][nx][ny] =  visited[z][x][y] + 1


# for a in range(h):
# 	for b in range(n):
# 		for c in range(m):
# 			if g[a][b][c] == 1 and not visited[a][b][c]:
# 				q.append((a,b,c))
# 				visited[a][b][c] = 1

# bfs()


# can = True

# day = 0

# for i in range(h):
# 	for j in range(n):
# 		for k in range(m):
# 			if not g[i][j][k]:
# 				can = False
# 			day = max(day,g[i][j][k])

# if can:
# 	print(day)
# else:
# 	print(-1)

# 성공
# import sys
# from collections import deque
# input = sys.stdin.readline

# m,n,h = map(int,input().split())


# dx = [-1,1,0,0,0,0]
# dy = [0,0,-1,1,0,0]
# dz = [0,0,0,0,-1,1]

# data = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
# queue = deque()

# #3차원 bfs문제
# def bfs():
# 	while queue:
# 		# 높이, x,y 순서
# 		z,x,y = queue.popleft()
# 		for i in range(6):
# 			nx = x + dx[i]
# 			ny = y + dy[i]
# 			nz = z + dz[i]
# 			if 0<=nx<n and 0<=ny<m and 0<=nz<h:
# 				if data[nz][nx][ny] == 0:
# 					data[nz][nx][ny] = data[z][x][y]+1
# 					queue.append((nz,nx,ny))

# for i in range(h):
# 	for j in range(n):
# 		for k in range(m):
# 			if data[i][j][k] == 1:
# 				queue.append((i,j,k))
# bfs()
# flag = 0
# result = 0
# for i in range(h):
# 	for j in range(n):
# 		for k in range(m):
# 			if data[i][j][k] == 0:
# 				flag = 1
# 			result = max(result,data[i][j][k])
# if flag == 1:
# 	print(-1)
# else:
# 	print(result-1)


# 탈출
# https://www.acmicpc.net/problem/3055

from collections import deque

import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]


r,c = map(int,input().split())

