maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
# maps = ["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]
from collections import deque

def chk(board):
	l = []
	s = []
	e = []
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == 'S':
				s.append([i,j])
			elif board[i][j] == 'E':
				e.append([i,j])
			elif board[i][j] == 'L':
				l.append([i,j])
	return (s[0],e[0],l[0])

dx = [-1,1,0,0]
dy = [0,0,-1,1]



def bfs(q,start,end,target,maps):
	n = len(maps)
	m = len(maps[0])
	visited = [[0] * m for _ in range(n)]
	q = deque()
	q.append((start[0],start[1]))
	while q:
		x,y = q.popleft()
		if maps[x][y] == target:
			return visited[end[0]][end[1]]
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0<= nx < len(maps) and 0<= ny < len(maps[0]):
				if not visited[nx][ny] and maps[nx][ny] != 'X':
					visited[nx][ny] = visited[x][y] + 1
					q.append((nx,ny))
	return False

def solution(maps):

	q = deque()
	start,end,la = chk(maps)

	s_l = bfs(q,start,la,'L',maps)
	l_e = bfs(q,la,end,'E',maps)

	if not s_l or not l_e:
		return -1
	else:
		return l_e + s_l

print(solution(maps))



# maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
# # maps = ["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]
# from collections import deque

# def chk(board):
# 	l = []
# 	s = []
# 	e = []
# 	for i in range(len(board)):
# 		for j in range(len(board[i])):
# 			if board[i][j] == 'S':
# 				s.append([i,j])
# 			elif board[i][j] == 'E':
# 				e.append([i,j])
# 			elif board[i][j] == 'L':
# 				l.append([i,j])
# 	return (s[0],e[0],l[0])

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]



# def bfs(q,start,end,visited,target,maps):
# 	n = len(maps)
# 	m = len(maps[0])
# 	visited = [[0] * m for _ in range(n)]
# 	q = deque()
# 	q.append((start[0],start[1]))
# 	while q:
# 		x,y = q.popleft()
# 		if maps[x][y] == target:
# 			return visited[end[0]][end[1]]
# 		for i in range(4):
# 			nx = x + dx[i]
# 			ny = y + dy[i]
# 			if 0<= nx < len(maps) and 0<= ny < len(maps[0]):
# 				if not visited[nx][ny] and maps[nx][ny] != 'X':
# 					visited[nx][ny] = visited[x][y] + 1
# 					q.append((nx,ny))
# 	return False

# def solution(maps):
# 	visited = [[0] * len(maps[0]) for _ in range(len(maps))]
# 	q = deque()
# 	start,end,la = chk(maps)

# 	s_l = bfs(q,start,la,visited,'L',maps)
# 	l_e = bfs(q,la,end,visited,'E',maps)

# 	if not s_l or not l_e:
# 		return -1
# 	else:
# 		return l_e

# print(solution(maps))

