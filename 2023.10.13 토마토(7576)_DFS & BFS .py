from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
g = []
for i in range(m):
	g.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[0] * n for _ in range(m)]



q = deque()

def bfs():
	while q:
		x,y = q.popleft()
		if g[x][y] == -1:
				continue
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
				if g[nx][ny] == 0:
					# visited[nx][ny] = visited[x][y]+1
					g[nx][ny] = g[x][y]+1
					# visited[nx][ny] = 1
					q.append((nx,ny))


for i in range(m):
	for j in range(n):
		if g[i][j] == 1:
			q.append((i,j))
bfs()


chk = True
day = 0

for i in range(m):
	for j in range(n):
		if g[i][j] == 0:
			chk = False
		day = max(day,g[i][j])
if chk:
	print(day-1)
else:
	print(-1)
