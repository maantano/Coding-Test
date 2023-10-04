# n = 7
# m = 7
# arr = [
# 	[2,0,0,0,1,1,0],
# 	[0,0,1,0,1,2,0],
# 	[0,1,1,0,1,0,0],
# 	[0,1,0,0,0,0,0],
# 	[0,0,0,0,0,1,1],
# 	[0,1,0,0,0,0,0],
# 	[0,1,0,0,0,0,0],
# ]

# # n,m = map(int,input().split())
# # arr = []
# # for i in range(n):
# # 	arr.append(map(int,input().split()))
# from collections import deque

# visited = [[0]*m for _ in range(n)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs(x,y):
# 	q = deque([(x,y)])
# 	visited[x][y] = 1
# 	wallCnt = 3
# 	safeCnt = 0
# 	while q:
# 		x,y = q.popleft()
# 		for i in range(4):
# 			nx = x + dx[i]
# 			ny = y + dy[i]

# 			# if arr[nx][ny] == 1 or arr[nx][ny] == 2:
# 			# 	continue

# 			if  nx <= 0 or nx >= n or ny <= 0 or ny >= m:
# 				continue
# 			if wallCnt != 0:
# 				if not arr[nx][ny] and not visited[nx][ny]:
# 					visited[nx][ny] +=1
# 					q.append((nx,ny))
# 					wallCnt-=1
# 	for i in range(n):
# 		for j in range(m):
# 			if arr[i][j] == 0:
# 				safeCnt +=1
# 	return safeCnt

# result = 0
# for i in range(n):
# 	for j in range(m):
# 		result = max(0,bfs(i,j))
# print(result)







import copy
from collections import deque
arr = []
n,m = map(int,input().split())

def make_wall(wallCnt):
	if wallCnt == 3:
		virus_spread()
		return
	for i in range(n):
		for j in range(m):
			if arr[i][j] == 0:
				arr[i][j] = 1
				make_wall(wallCnt+1)
				arr[i][j] = 0


dx = [0,0,1,-1]
dy = [1,-1,0,0]

def virus_spread():
	global answer
	q = deque()
	tmp_arr = copy.deepcopy(arr)

	for i in range(n):
		for j in range(m):
			if tmp_arr[i][j] == 2:
				q.append((i,j))
	while q:
		x,y = q.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			# if 0 <= nx < n and  0 <= ny < m and tmp_arr[nx][ny] == 0:
			# 	tmp_arr[nx][ny] = 2
			# 	q.append((nx,ny))
			if nx < 0 or nx >= n or ny < 0 or ny >= m:
				continue
			if tmp_arr[nx][ny] == 0:
				tmp_arr[nx][ny] = 2
				q.append((nx,ny))

	cnt = 0
	for i in range(n):
		cnt += tmp_arr[i].count(0)
	answer = max(answer,cnt)


for i in range(n):
	arr.append(list(map(int,input().split())))
answer = 0
make_wall(0)
print(answer)
