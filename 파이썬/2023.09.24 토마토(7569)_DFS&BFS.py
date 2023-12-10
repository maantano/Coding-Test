# # n,m,h = map(int,input().split())

# n = 5
# m = 3
# h = 2

# # g = [[]*n for _ in range(m)] * h

# # for i in range(m*h):
# # 	g[i] = list(map(int,input().split()))
# g = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
# print(g)

# path = [
# 	[1,0],
# 	[-1,0],
# 	[0,1],
# 	[0,-1],
# ]
# def start(g):
# 	for i in range(len(g)):
# 		if 1 in g[i]:
# 			return (i,g[i].index(1))


# day = 0

# def dfs(x,y):
# 	global day
# 	for i in range(4):
# 		move_x,move_y= path[i]
# 		newX = move_x + x
# 		newY = move_y + y
# 		if newX <= -1 or newX >= (m*h) or newY <= -1 or newY >= n:
# 			continue
# 		if g[newX][newY] == -1:
# 			continue
# 		if g[newX][newY] == 0:
# 			g[newX][newY] = 1
# 			dfs(newX,newY)
# x,y = start(g)
# def dfs(x,y):
# 	global day
# 	for i in range(4):
# 		move_x,move_y= path[i]
# 		newX = move_x + x
# 		newY = move_y + y
# 		if newX <= -1 or newX >= (m*h) or newY <= -1 or newY >= n:
# 			continue
# 		if g[newX][newY] == -1:
# 			continue
# 		if g[newX][newY] == 0:
# 			g[newX][newY] = 1
# 			# dfs(newX,newY)
# 	day+=1
# 	dfs(x,y)
# dfs(x,y)


# for i in g:
# 	if 0 in i:
# 		print(-1)
# 	else:
# 		print(day)



import sys
from collections import deque
input = sys.stdin.readline

M,N,H = map(int,input().split())
g = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]


dx =  [1,-1,0,0,0,0]
dy =  [0,0,1,-1,0,0]
dz =  [0,0,0,0,1,-1]

q = deque()

def BFS():
	while q:
		z,x,y = q.popleft()
		for i in range(6):
			newZ = dz[i] + z
			newX = dx[i] + x
			newY = dy[i] + y
			if 0 <= newX < N and 0 <= newY < M and 0 <= newZ < H:
				if g[newZ][newX][newY] == 0:
					g[newZ][newX][newY] = g[z][x][y] +1
					q.append((newZ,newX,newY))


for i in range(H):
	for j in range(N):
		for k in range(M):
			if g[i][j][k] == 1:
				q.append((i,j,k))

BFS()


chk = True
day =0
for i in range(H):
	for j in range(N):
		for k in range(M):
			if g[i][j][k] == 0:
				chk = False
			day = max(day,g[i][j][k])

if chk:
	print(day-1)
else:
	print(-1)
