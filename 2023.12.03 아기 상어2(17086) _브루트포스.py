
# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# g = [list(map(int,input().split())) for _ in range(n)]

# dx = [-1,1,0,0,-1,-1,1,1]
# dy = [0,0,-1,1,-1,1,-1,1]


# # dp=[[0] * (m+1) for _ in range(n+1)]

# from collections import deque
# visited = [[0] * m for _ in range(n)]
# def bfs(x,y):
# 	q = deque([(x,y)])
# 	visited[x][y] = 1
# 	cnt = 0
# 	while q:
# 		x,y = q.popleft()
# 		for i in range(8):
# 			nx = x + dx[i]
# 			ny = y + dy[i]

# 			if 0<= nx < n and 0<= ny < m:
# 				if not visited[nx][ny]:
# 					# visited[nx][ny] = 1
# 					visited[nx][ny] = visited[x][y]+1
# 					q.append((nx,ny))
# 					cnt+=1
# 				elif g[nx][ny]:
# 					return cnt
# 	return cnt

# answer = 0
# for i in range(n):
# 	for j in range(m):
# 		if g[i][j]:
# 			bfs(i,j)
# for i in range(n):
# 	answer = max(answer,max(visited[i]))
# print(answer-1)



import sys
input = sys.stdin.readline

n,m = map(int,input().split())
g = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]

from collections import deque
visited = [[0] * m for _ in range(n)]
q = deque()
def bfs():
	# visited[x][y] = 1
	# cnt = 0
	while q:
		x,y = q.popleft()
		for i in range(8):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0<= nx < n and 0<= ny < m:
				if not g[nx][ny]:
					g[nx][ny] = g[x][y]+1
					q.append((nx,ny))

for i in range(n):
	for j in range(m):
		if g[i][j]:
			q.append((i,j))

bfs()
answer = 0
for i in range(n):
	answer = max(max(g[i]),answer)
print(answer-1)
