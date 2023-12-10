n,m = map(int,input().split())
arr = [[0] * 7 for _ in range(n)]
for i in range(n):
	arr[i] = list(map(int,input().split()))
from collections import deque

move = [
	[1,0],
	[-1,0],
	[0,1],
	[0,-1],
]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
	q = deque([(x, y)])
	visited[x][y] = 1
	seaList = []
	while q:
		x,y = q.popleft()
		sea = 0
		for i in range(4):
			newX = x + dx[i]
			newY = y + dy[i]
			if 0 <= newX < n and 0 <= newY < m:
				if not arr[newX][newY]:
					sea+=1
				elif arr[newX][newY] and not visited[newX][newY]:
					q.append((newX,newY))
					visited[newX][newY] = 1
		if sea > 0:
			seaList.append((x,y,sea))
	for x,y,sea,in seaList:
		arr[x][y] = max(0,arr[x][y]-sea)
	return 1

ice = []

for i in range(n):
	for j in range(m):
		if arr[i][j]:
			ice.append((i,j))
year = 0

while ice:
	visited = [[0]* m for _ in range(n)]
	delList = []
	group = 0
	for i,j in ice:
		if arr[i][j] and not visited[i][j]:
			group += bfs(i,j)
		if arr[i][j] == 0:
			delList.append((i,j))
	if group > 1:
		print(year)
		break
	ice = sorted(list(set(ice)-set(delList)))
	year += 1

if group < 2:
	print(0)

			# if newX <= 0 or newX >=n or newY <= 0 or newY >=n:
			# 	cnt+=1
			# if arr[newX][newY] == 0:
			# 	# arr[newX][newX] -= 1
			# 	visited[newX][newY] = 1
			# 	q.append((newX,newY))





