import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().rstrip())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

from collections import deque

visited = [[0]*n for _ in range(n)]

def bfs():
	q = deque([(0,0)])
	visited[0][0] = 1
	cnt = 1
	while q:
		x,y = q.popleft()
		if x == n-1 and y == n-1:
			return visited[x][y] -1

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx < n and 0<= ny < n:
				if not visited[nx][ny]:
					if arr[nx][ny]:
						q.appendleft((nx,ny))
						visited[nx][ny] = visited[x][y]
					else:
						q.append((nx,ny))
						arr[nx][ny]= 1
						visited[nx][ny] = visited[x][y] + 1
print(bfs())
