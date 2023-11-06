from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr = []
for i in range(n):
	arr.append(list(map(int,input().rstrip())))

visited = [[0]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs():
	q = deque([(0,0)])
	visited[0][0] = 1

	while q:
		x,y = q.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if nx < 0 or nx >= n or ny < 0 or ny >= m:
				continue
			if not visited[nx][ny] and arr[nx][ny]:
				visited[nx][ny] = visited[x][y]+1
				q.append((nx,ny))
	print(visited[n-1][m-1])
bfs()
