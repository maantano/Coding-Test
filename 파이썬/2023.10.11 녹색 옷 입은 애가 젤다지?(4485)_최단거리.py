# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4
# 0

import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dijkstra():
	q = []
	heapq.heappush(q,(g[0][0],0,0))
	distance[0][0] = 0

	while q:
		cost,x,y = heapq.heappop(q)
		if x == n - 1 and y == n - 1:
			print(f'Problem {count}: {distance[x][y]}')
			break

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0<= nx < n and 0<= ny < n:
				newCost = cost + g[nx][ny]
				if distance[nx][ny] > newCost:
					distance[nx][ny] = newCost
					heapq.heappush(q,(newCost,nx,ny))


count = 1
while True:
	n = int(input())
	if n == 0:
		break
	g = [list(map(int, input().split())) for _ in range(n)]
	distance = [[INF] * n for _ in range(n)]
	dijkstra()
	count+=1
