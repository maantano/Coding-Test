n,m = map(int,input().split())

arr = [ list(map(int,input().split())) for i in range(n) ]
visited =[[0]*m for i in range(n)]
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]


cnt = 0
def bfs(x,y):
	global cnt
	q = deque([(x,y)])
	visited[x][y] = 1
	biggest = 1
	while q:
		x,y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0<= nx < n and 0 <=ny < m:
				if not visited[nx][ny] and arr[nx][ny] == 1:
					visited[nx][ny] = 1
					q.append((nx,ny))
					biggest+=1

	cnt+=1
	return biggest
result2 = 0
for i in range(n):
	for j in range(m):
		if arr[i][j] == 1 and not visited[i][j]:
			result2 = max(result2,bfs(i,j))
print(cnt)
print(result2)
