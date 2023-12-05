



# white,black = 0,0
# def dfs(x,y,l):
# 	global white,black

# 	if white == 5:
# 		print('white')
# 		return (2,l)
# 	elif black == 5:
# 		print('black')
# 		return (1,l)
# 	visited[x][y] = 1
# 	for i in range(8):
# 		nx = x + dx[i]
# 		ny = y + dy[i]
# 		if 0<= nx < 19 and 0<= ny < 19:
# 			if not visited[nx][ny]:
# 				visited[nx][ny] = 1
# 				if g[nx][ny] == 1:
# 					black+=1
# 				elif g[nx][ny] == 2:
# 					white+=1
# 				l.append((nx,ny))
# 				dfs(nx,ny,l)
# 				if g[nx][ny] == 1:
# 					black-=1
# 				elif g[nx][ny] == 2:
# 					white-=1
# 				l.pop()
# 				visited[nx][ny] = 0
# 	visited[x][y] =0

# dfs(0,0,[(0,0)])


import sys
input = sys.stdin.readline
g = [list(map(int,input().split())) for _ in range(19)]
dx = [0,1,1,-1]
dy = [1,0,1,1]
find = False
def bfs(x,y):
	global find

	target = g[x][y]

	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		cnt = 1

		while 0<=nx < 19 and 0<= ny < 19 and g[nx][ny] == target:
			cnt+=1
			if cnt == 5:
				if 0 <= x - dx[i] < 19 and 0<= y-dy[i] < 19 and g[x-dx[i]][y-dy[i]] == target:
					break
				if 0 <= nx + dx[i] < 19 and 0<= ny+dy[i] < 19 and g[nx+dx[i]][ny+dy[i]] == target:
					break

				print(target)
				print(x+1,y+1)
				find = True
				return
			nx += dx[i]
			ny += dy[i]

for i in range(19):
	for j in range(19):
		if g[i][j] != 0:
			bfs(i,j)


if not find:
	print(0)
