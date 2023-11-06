from collections import deque
import sys
input = sys.stdin.readline

t = int(input().rstrip())

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1]

answer = []

for i in range(t):
	cnt = 0
	l = int(input().rstrip())

	g = [[0] * l for _ in range(l)]
	start_x,start_y = map(int,input().split())
	end_x,end_y = map(int,input().split())

	q = deque([(start_x,start_y)])
	g[start_x][start_y] = 1

	while q:
		x,y, = q.popleft()
		if x == end_x and y == end_y:
			print(g[x][y]-1)
			break
		for i in range(8):
			nx = x + dx[i]
			ny = y + dy[i]

			# if nx<0 or nx >= l or ny < 0 or ny >= l:
			# 	continue
			if 0<= nx < l and 0<= ny < l:
			if not g[nx][ny]:
				cnt+=1
				g[nx][ny] = g[x][y] + 1
				q.append((nx,ny))


