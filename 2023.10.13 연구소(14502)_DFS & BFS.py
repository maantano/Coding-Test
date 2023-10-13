import sys
input = sys.stdin.readline
import copy
from collections import deque

n,m = map(int,input().split())
# visited = [[0]*m for _ in range(n)]
g = []


def makeWall(cnt):
	if cnt == 3:
		virus()
		return
	for i in range(n):
		for j in range(m):
			if g[i][j] == 0:
				g[i][j] = 1
				makeWall(cnt+1)
				g[i][j] = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def virus():
	global answer
	q = deque()
	tmp_virus= copy.deepcopy(g)

	for i in range(n):
		for j in range(m):
			if tmp_virus[i][j] == 2:
				q.append((i,j))

	while q:
		x,y = q.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			# if nx < 0 or nx >= n or ny < 0 or ny >= m:
			# 	continue
			# if tmp_virus[nx][ny] == 0:
			# 	tmp_virus[nx][ny] = 2
			# 	q.append((nx,ny))

			if 0 <= nx < n and 0 <= ny < m and tmp_virus[nx][ny] == 0:
				# if tmp_virus[nx][ny] == 0:
				tmp_virus[nx][ny] = 2
				q.append((nx,ny))
	cnt = 0
	for i in range(n):
		cnt += tmp_virus[i].count(0)
	answer = max(answer,cnt)

for i in range(n):
	g.append(list(map(int,input().split())))

answer = 0
makeWall(0)
print(answer)



