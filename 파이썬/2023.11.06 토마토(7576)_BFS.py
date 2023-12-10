from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr = []
for i in range(m):
	arr.append(list(map(int,input().split(' '))))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
# print(arr)
q = deque()

def bfs():

	while q:
		x,y = q.popleft()
		if arr[x][y] == -1:
			continue
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < m  and 0<= ny < n:
				if not arr[nx][ny]:
					q.append((nx,ny))
					arr[nx][ny] = arr[x][y] + 1

for i in range(m):
	for j in range(n):
		if arr[i][j] == 1:
			q.append((i,j))
bfs()
chk = True
day = 0


for i in range(m):
	for j in range(n):
		if arr[i][j] == 0:
			chk=False
		day = max(day,arr[i][j])
if chk:
	print(day-1)
else:
	print(-1)





# if visited[0][0]== 0 or visited[m-1][n-1] == 0:
# 	print(-1)
# else:
# 	print(max(visited[0][0]-1,visited[m-1][n-1]-1))


# from collections import deque
# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# visited = [[0] * n for _ in range(m)]
# arr = []
# for i in range(m):
# 	arr.append(list(map(int,input().split(' '))))

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# # print(arr)

# def bfs(x,y):
# 	q=deque([(x,y)])
# 	visited[x][y] = 1
# 	cnt= 0
# 	while q:
# 		x,y = q.popleft()
# 		for i in range(4):
# 			nx = x + dx[i]
# 			ny = y + dy[i]
# 			if 0 <= nx < m  and 0<= ny < n:
# 				if arr[nx][ny] == -1:
# 					continue
# 				if not visited[nx][ny] and arr[nx][ny] == 0:
# 					q.append((nx,ny))
# 					arr[nx][ny] = 1
# 					visited[nx][ny] = visited[x][y] + 1
# 	# 				cnt+=1
# 	# return cnt



# for i in range(m):
# 	for j in range(n):
# 		if arr[i][j] == 1:
# 			bfs(i,j)
# print(arr)
# print(visited)

# if visited[0][0]== 0 or visited[m-1][n-1] == 0:
# 	print(-1)
# else:
# 	print(max(visited[0][0]-1,visited[m-1][n-1]-1))
