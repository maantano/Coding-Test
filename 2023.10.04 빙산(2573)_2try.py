n,m = map(int,input().split())
arr = [[0]* m for _ in range(n)]

for i in range(n):
	arr[i] = list(map(int,input().split()))
from collections import deque


dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(x,y):
	q = deque([(x,y)])
	visitied[x][y] = 1
	seaList = []

	while q:
		x,y = q.popleft()
		sea = 0
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0<= nx < n and 0<= ny < m:
				if not arr[nx][ny]:
					sea +=1
				elif arr[nx][ny] and not visitied[nx][ny]:
					visitied[nx][ny] = 1
					q.append((nx,ny))
		if sea > 0:
			seaList.append((x,y,sea))

	for x,y,sea in seaList:
		arr[x][y] = max(0,arr[x][y] - sea)
	return 1



ice = []

for i in range(n):
	for j in range(m):
		if arr[i][j]:
			ice.append((i,j))
year = 0

while ice:
	visitied = [[0] * m for _ in range(n)]
	delList = []
	group = 0

	for i,j in ice:
		if arr[i][j] and not visitied[i][j]:
			group += bfs(i,j)
		if arr[i][j] == 0:
			delList.append((i,j))
	if group >1:
		print(year)
		break
	ice = sorted(list(set(ice)-set(delList)))
	year+=1

if group < 2:
	print(0)

