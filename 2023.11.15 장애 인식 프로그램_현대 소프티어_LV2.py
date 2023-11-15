import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
visited = [[0] * n for _ in range(n)]
arr = [list(map(int,input().rstrip())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
	q = deque([(x,y)])
	visited[x][y] = 1
	cnt = 1
	while q:
		x,y = q.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0<= nx < n and 0 <= ny < n:
				if not visited[nx][ny] and arr[nx][ny]:
					arr[nx][ny] = 0
					visited[nx][ny] = 1
					cnt+=1
					q.append((nx,ny))
	return cnt
answer = []
for i in range(n):
	for j in range(n):
		if arr[i][j] == 1:
			answer.append(bfs(i,j))

print(len(answer))
for i in sorted(answer):
	print(i)




