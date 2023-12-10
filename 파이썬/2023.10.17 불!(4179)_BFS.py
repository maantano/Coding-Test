# 미로에서의 지훈이의 위치와 불이 붙은 위치를 감안해서 지훈이가 불에 타기전에 탈출할 수 있는지의 여부,
# 그리고 얼마나 빨리 탈출할 수 있는지를 결정해야한다

# 지훈이와 불은 매 분마다 한칸씩 수평또는 수직으로(비스듬하게 이동하지 않는다) 이동한다.

# #: 벽
# .: 지나갈 수 있는 공간
# J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
# F: 불이 난 공간

def start(arr):
	for i in range(n):
		for j in range(m):
			if arr[i][j] == 'J':
				return (i,j)
def startF(arr):
	for i in range(n):
		for j in range(m):
			if arr[i][j] == 'F':
				return (i,j)

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,xf,yf):
	q = deque([(x,y)])
	visited[x][y] = 1
	cnt = 0
	# lsx,lsy =0,0
	while q:
		x,y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			nxf = xf + dx[i]
			nyf = yf + dy[i]
			if 0<= nx < n and 0<= ny <m:
				if arr[nx][ny] != '#' and arr[nx][ny] != 'F' and not visited[nx][ny]:
					visited[nx][ny] = 1
					q.append((nx,ny))
					cnt += 1
			if 0<= nxf < n and 0<= nyf < m:
				arr[nxf][nyf] = 'F'

		lsx,lsy = x,y
		if lsx == 4 or lsy == 4:
			print(cnt)
			exit()
	print('IMPOSSIBLE')

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
visited = [[0]*m for i in range(n)]
arr = [list(map(str,input().rstrip())) for _ in range(n)]
x,y = start(arr)
xf,yf = startF(arr)
bfs(x,y,xf,yf)
