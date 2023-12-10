# n = 4
# m = 6

n,m = map(int,input().split())

# g = [
# 	[1,0,1,1,1,1],
# 	[1,0,1,0,1,0],
# 	[1,0,1,0,1,1],
# 	[1,1,1,0,1,1],
# ]

g=[]

for i in range(n):
	g.append(list(map(int,input())))


path = [
	[-1,0],
	[1,0],
	[0,-1],
	[0,1]
]


from collections import deque

def bfs(x,y):
	q= deque()
	q.append((x,y))
	while q:
		x,y = q.popleft()
		for i in range(4):
			move_x,move_y = path[i]
			newX = x + move_x
			newY = y + move_y

			if newX <= -1 or newX >=n or newY <= -1 or newY >=m:
				continue
			if g[newX][newY] == 0:
				continue
			if g[newX][newY] == 1:
				g[newX][newY] = g[x][y]+1
				q.append((newX,newY))
	print(g[n-1][m-1])


bfs(0,0)
