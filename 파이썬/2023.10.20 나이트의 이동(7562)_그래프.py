import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
dx = [+2, +1, -1, -2, -2, -1, +1, +2]
dy = [+1, +2, +2, +1, -1, -2, -2, -1]


def bfs(x,y,targetX,targetY):
	q = deque([(x,y)])
	while q:
		curX,curY = q.popleft()
		if curX == targetX and curY == targetY:
			print(visited[curX][curY]-1)
			return True

		for i in range(8):
			nx = curX + dx[i]
			ny = curY + dy[i]
			if 0 <= nx < l and 0 <= ny < l:
				if not visited[nx][ny]:
					visited[nx][ny] = visited[curX][curY]+1
					q.append((nx,ny))
	return False

for i in range(t):
	l = int(input())
	visited = [[0] * (l) for _ in range(l)]
	x,y = map(int,input().split())
	targetX,targetY = map(int,input().split())
	visited[x][y] = 1
	bfs(x,y,targetX,targetY)

