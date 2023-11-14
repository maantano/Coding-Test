
import sys
input = sys.stdin.readline
n,m,t = map(int,input().split())

arr = [[1] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]

for _ in range(t):
	a,b = map(int,input().split())
	arr[a-1][b-1] = 0

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = 0
answerl = []
def bfs(x,y,visited):
	cnt=1
	q = deque([(x,y)])
	visited[x][y] = 1

	while q:
		x,y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0<= nx < n and 0<= ny <m:
				if not visited[nx][ny] and not arr[nx][ny]:
					q.append((nx,ny))
					visited[nx][ny] = visited[x][y] + 1
					cnt+=1
	return cnt


for i in range(n):
	for j in range(m):
		if arr[i][j] == 0:
			answer = max(answer,bfs(i,j,visited))
print(answer)


# [
#  [1, 0, 0, 0],
#  [0, 0, 0, 0],
#  [0, 0, 0, 0]
#  ]
# [
# 	[1, 0, 0, 0],
# 	[0, 1, 2, 0],
# 	[3, 2, 0, 0]]
# [[1, 0, 0, 0], [0, 1, 1, 0], [3, 2, 0, 0]]
# [[1, 0, 0, 0], [0, 1, 1, 0], [1, 2, 0, 0]]
# [[1, 0, 0, 0], [0, 1, 1, 0], [1, 1, 0, 0]]
