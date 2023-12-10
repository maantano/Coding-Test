import sys
input = sys.stdin.readline
c,r = map(int,input().split())
target = int(input())

if target > c*r :
	print(0)
	exit()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

direction=x=y=0


grid = [[0]*c for _ in range(r)]
for seat in range(1,c*r+1):
	if seat == target:
		print(y+1,x+1)
		break
	else:
		grid[x][y] = seat

		x += dx[direction]
		y += dx[direction]

		if x<0 or y < 0 or x>=r or y>= c or grid[x][y]:

			x -= dx[direction]
			y -= dx[direction]
			direction = (direction+1) % 4
			x += dx[direction]
			y += dx[direction]


