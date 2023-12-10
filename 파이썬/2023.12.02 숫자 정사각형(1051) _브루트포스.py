# # import sys
# # input = sys.stdin.readline


# # n,m = map(int,input().split())
# # g = [list(map(int,input().rstrip())) for _ in range(n)]

# # dx = [1,0]
# # dy = [0,1]

# # # dx[(direction+1) % 4]


# # answer = []
# # if n == 1:
# # 	print(1)
# # else:
# # 	# print(1)
# # 	direction = x = y = 0
# # 	for i in range(n):
# # 		cnt=0
# # 		for j in range(m):
# # 			# chk = g[i][j]
# # 			if g[i + dx[(direction+1)%2]][j+dy[(direction+1)%2]] == g[i][j]:
# # 				cnt+=1
# # 				continue


















# from collections import deque

# n,m = map(int,input().split())
# g = [list(map(int,input().rstrip())) for _ in range(n)]


# dx = [1,0]
# dy = [0,1]

# def bfs(startX,startY):
# 	q = deque([(startX,startY)])
# 	tmpCnt = 0
# 	realCnt = 0
# 	width = 0
# 	height = 0
# 	print(g[startX][startY])
# 	while q:
# 		x,y = q.popleft()
# 		for i in range(2):
# 			nx = x + dx[i]
# 			ny = y + dy[i]
# 			if 0 <= nx < n and 0 <= ny < m and nx <= ny and ny <= nx:
# 				print('g[startX][startY] ===>',g[startX][startY])
# 				print('g[nx][ny] ===>',g[nx][ny])
# 				print('g[ny][nx] ===>',g[ny][nx])
# 				if g[startX][startY] == g[nx][ny] == g[ny][nx] == g[startY][startX]:
# 					realCnt = tmpCnt
# 					width = nx
# 					height = ny
# 				q.append((nx,ny))
# 				tmpCnt+=1
# 	print('realCnt,width,height ===>',realCnt,width,height)



# for i in range(n):
# 	for j in range(m):
# 		bfs(i,j)



def find_squre(s):
	for i in range(N-s+1):
		for j in range(M-s+1):
			if numbers[i][j] == numbers[i][j+s-1] == numbers[i+s-1][j] == numbers[i+s-1][j+s-1]:
				return True
	return False
N, M = map(int, input().split())
numbers = [list(map(int, list(input()))) for _ in range(N)]
size = min(N,M)
for k in range(size, 0, -1):
	if find_squre(k):
		print(k**2)
		break
