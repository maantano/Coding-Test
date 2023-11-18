import sys
input = sys.stdin.readline

# maps = ["X591X","X1X5X","X231X", "1XXX1"]
maps = ["XXX","XXX","XXX"]
n = len(maps)
m = len(maps[0])
arr = []
for i in range(n):
	i = list(map(str,maps[i]))
	arr.append(i)

visited = [[0] * m for i in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

from collections import deque
answer =[]
def bfs(x,y):
	q = deque([(x,y)])
	visited[x][y] = int(arr[x][y])
	tmp = int(arr[x][y])
	arr[x][y] ='X'
	while q:
		x,y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0<=nx < n and 0<= ny < m:
				if not visited[nx][ny] and arr[nx][ny] != 'X':
					visited[nx][ny] = 1
					tmp+=int(arr[nx][ny])
					q.append((nx,ny))
					arr[nx][ny] ='X'
	answer.append(tmp)

for i in range(n):
	for j in range(m):
		if arr[i][j].isdigit():
			bfs(i,j)

if len(answer) == 0:
	print(-1)
else:
	print(answer)
