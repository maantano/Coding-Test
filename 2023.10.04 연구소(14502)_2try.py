n,m = map(int,input().split())

arr = []

def wallCnt(cnt):
	if cnt == 3:
		virusSpread()
		return
	for i in range(n):
		for j in range(m):
			if arr[i][j] == 0:
				arr[i][j] = 1
				wallCnt(cnt+1)
				arr[i][j] = 0

from collections import deque
import copy

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = 0
def virusSpread():
	global result
	q = deque()
	tmpArr= copy.deepcopy(arr)
	# virusList = [(x,y) for i in range(n) for j in range(m) if tmpArr[x][y] == 2]
	# q.append(list(virusList))
	# visited = [[0]*m for _ in range(n)]

	for i in range(n):
		for j in range(m):
			if tmpArr[i][j] == 2:
				q.append((i,j))

	while q:
		x,y  = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if nx < 0 or nx >=n or ny <0 or ny >= m:
			# if 0<= nx < n or 0<= ny < m:
				continue
			if not tmpArr[nx][ny]:
					tmpArr[nx][ny] = 2
					# visited[nx][ny] = 1
					q.append((nx,ny))
			# if not tmpArr[nx][ny] and not visited[nx][ny]:
			# 	tmpArr[nx][ny] = 2
			# 	visited[nx][ny] = 1
			# 	q.append((nx,ny))

	cnt = 0
	for i in range(n):
		for j in range(m):
			if tmpArr[i][j] == 0:
				cnt+=1
	result = max(cnt,result)

	# cnt = 0
	# for i in range(n):
	# 	cnt += tmpArr[i].count(0)
	# result = max(result,cnt)


for i in range(n):
	arr.append(list(map(int,input().split())))

wallCnt(0)
print(result)
