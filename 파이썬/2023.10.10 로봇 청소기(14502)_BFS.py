# # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
# # 현재 칸의 주변
# # $4$칸 중 청소되지 않은 빈 칸이 없는 경우,
# # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
# # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
# # 현재 칸의 주변
# # $4$칸 중 청소되지 않은 빈 칸이 있는 경우,
# # 반시계 방향으로
# # $90^\circ$ 회전한다.
# # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
# # 1번으로 돌아간다.
# # 북,서,남,동
# path = [
# 	[-1,0],
# 	[0,-1],
# 	[1,0],
# 	[0,1],
# ]


# n,m = map(int,input().split())
# r,c,way = map(int,input().split())
# g = []
# for i in range(n):
# 	g.append(list(map(int,input().split())))
# visited = [[0]*m for _ in range(n)]

# cnt = 0
# from collections import deque
# def bfs(x,y,way):
# 	global cnt
# 	q = deque()
# 	q.append((x,y,way))
# 	visited[x][y] = 1
# 	while q:
# 		x,y,way = q.popleft()
# 		way = (way+3) % 4
# 		nx = x + path[way][0]
# 		ny = y + path[way][1]
# 		# if nx < 0 or nx >= n or ny < 0 or ny >= m:
# 		# 	continue
# 		if 0<= nx < n and 0<= ny < m and g[nx][ny] == 0:
# 			# way = (way+1) % 4
# 			if not visited[nx][ny]:
# 				q.append((nx,ny,way))
# 				visited[nx][ny] = 1
# 				cnt+=1
# 			else:
# 				if g[x-path[way][0]][y-path[way][1]] == 1:
# 					print(cnt)
# 					break
# 				else:
# 					q.append((x-path[way][0],y-path[way][1],way))
# bfs(r,c,way)


# 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
# 현재 칸의 주변
# $4$칸 중 청소되지 않은 빈 칸이 없는 경우,
# 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
# 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
# 현재 칸의 주변
# $4$칸 중 청소되지 않은 빈 칸이 있는 경우,
# 반시계 방향으로
# $90^\circ$ 회전한다.
# 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
# 1번으로 돌아간다.
# 북,서,남,동
path = [
	[-1,0],
	[0,-1],
	[1,0],
	[0,1],
]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

n,m = map(int,input().split())
r,c,way = map(int,input().split())
g = []
for i in range(n):
	g.append(list(map(int,input().split())))
visited = [[0]*m for _ in range(n)]

cnt = 1


visited[r][c] = 1
while True:
	flag = 0

	for _ in range(4):
		way = (way+3) % 4
		nx = r + dr[way]
		ny = c + dc[way]
		if 0<= nx < n and 0<= ny < m and g[nx][ny] == 0:
			if not visited[nx][ny]:
				r = nx
				c = ny
				visited[nx][ny] = 1
				cnt+=1
				flag = 1
				break
	if flag == 0:
		if g[r-dr[way]][c-dc[way]] == 1:
			print(cnt)
			break
		else:
			r, c = r-dr[way], c-dc[way]

