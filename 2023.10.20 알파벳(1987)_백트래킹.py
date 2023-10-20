# import sys
# input = sys.stdin.readline

# R,C = map(int,input().split())

# arr = [list(map(str,input())) for _ in range(R)]
# alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# d = {i:0 for idx,i in enumerate(alpha)}
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# from collections import deque
# visited = [[0] * C for _ in range(R)]
# cnt = 0
# def chk(x,y):
# 	global cnt
# 	q = deque([(x,y)])
# 	visited[x][y] = 1
# 	d[arr[x][y]] = 1
# 	while q:
# 		x,y = q.popleft()

# 		for i in range(4):
# 			nx = x + dx[i]
# 			ny = y + dy[i]
# 			if d[arr[nx][ny]] == 0:
# 				d[arr[nx][ny]] = 1
# 			else:
# 				d[arr[nx][ny]] +=1

# 			if 0<= nx < R and 0<= ny < C and d[arr[nx][ny]] <=1:
# 				if not visited[nx][ny]:
# 					q.append((nx,ny))
# 					visited[nx][ny] = 1
# 					cnt+=1

# chk(0,0)
# print(cnt)




# -----------시간 초과
# import sys
# input = sys.stdin.readline

# r,c = map(int,input().split())
# arr = [list(input()) for _ in range(r)]
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# from collections import deque
# answer  =1
# def bfs(x,y):
# 	global answer
# 	q = deque()
# 	q.append([x,y,arr[x][y]])
# 	while q:
# 		x,y,ans = q.popleft()
# 		for i in range(4):
# 			nx = x + dx[i]
# 			ny = y + dy[i]
# 			if 0<= nx < r and 0<= ny < c and arr[nx][ny] not in ans:
# 				q.append([nx,ny,ans+arr[nx][ny]])
# 				print(len(ans))
# 				answer=max(answer,len(ans)+1)

# bfs(0,0)
# print(answer)



# set으로 변경 deque 는 O(N) // set 은 O(1) 그래서 set으로 풀어야한다.
import sys
input = sys.stdin.readline
r,c = map(int,input().split())
arr = [list(input()) for _ in range(r)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

answer = 1
def bfs(x,y):
	global answer
	q = set([(x,y,arr[x][y])])

	while q:
		x,y,ans = q.pop()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0<= nx < r and 0<= ny <c and arr[nx][ny] not in ans:
				q.add((nx,ny,ans+arr[nx][ny]))
				answer = max(answer,len(ans)+1)
bfs(0,0)
print(answer)


# DFS - pypy3

# import sys
# from collections import deque
# input = sys.stdin.readline

# r,c = map(int,input().split())
# arr = [list(input()) for _ in range(r)]

# visited = [0] * 26
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# maxi = 0

# def dfs(x,y,cnt):
# 	global maxi
# 	maxi = max(cnt,maxi)
# 	for i in range(4):
# 		nx = x + dx[i]
# 		ny = y + dy[i]

# 		if 0<= nx < r and 0<= ny < c and visited[ord(arr[nx][ny]) -65] == 0:
# 			visited[ord(arr[nx][ny])-65] = 1
# 			dfs(nx,ny,cnt+1)
# 			visited[ord(arr[nx][ny])-65] = 0

# visited[ord(arr[0][0])-65] = 1
# dfs(0,0,1)

# print(maxi)


