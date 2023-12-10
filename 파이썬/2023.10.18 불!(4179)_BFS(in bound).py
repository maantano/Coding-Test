import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
f_queue, j_queue = deque(), deque()    # declare fire, jihoon queue
f_visited, j_visited = [[0] * m for _ in range(n)], [[0] * m for _ in range(n)]    # declare fire, jihoon visited

for i in range(n):
	for j in range(m):
		if arr[i][j] == 'F':
			f_queue.append((i, j))
		elif arr[i][j] == 'J':
			j_queue.append((i, j))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
	while f_queue:
		x,y = f_queue.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0<= nx < n and 0<= ny < m:
				if not f_visited[nx][ny] and arr[nx][ny] != '#':
					f_visited[nx][ny] = f_visited[x][y] + 1
					f_queue.append((nx,ny))
	while j_queue:
		x,y = j_queue.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0<= nx < n and 0<= ny < m:
				if arr[nx][ny] != '#' and not j_visited[nx][ny]:
					if not f_visited[nx][ny] or f_visited[nx][ny] > j_visited[x][y]+1:
						j_visited[nx][ny] = j_visited[x][y]+1
						j_queue.append((nx,ny))
			else:
				return j_visited[x][y] + 1
	return 'IMPOSSIBLE'
print(bfs())
