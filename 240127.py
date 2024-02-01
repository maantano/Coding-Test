# import sys
# import math
# input = sys.stdin.readline

# dp =[0,1]

# n = int(input())
# for i in range(2,n+1):
# 	minValue = 1e9
# 	for j in range(1,int(math.sqrt(i)+1)):
# 		minValue = min(minValue,dp[i-j**2])
# 	dp.append(minValue+1)
# print(dp[n])




# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# num = list(map(int,input().split()))

# sum = 0
# reminder = [0] * m

# for i in range(n):
# 	sum+=num[i]
# 	reminder[sum%m] += 1

# result = reminder[0]
# for i in reminder:
# 	result += i * (i-1) // 2
# print(result)


# 치킨 배달
# https://www.acmicpc.net/problem/15686
# import sys
# from collections import deque

# input = sys.stdin.readline
# n, m = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(n)]

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]




# # def bfs(x,y):
# # 	q = deque([x,y])
# # 	while q:
# # 		for i in range(4):
# # 			nx = dx[i] + x
# # 			ny = dy[i] + y

# # 			if 0<= nx < n and 0<= ny < n:
# # 				if not visited[nx][ny]:

# # 					visited[nx][ny] = visited[x][y] + 1
# # 					if arr[nx][ny] == 1:
# # 						visited[nx][ny] = min(visited[nx][ny],visited[x][y])
# # 					q.append(([nx,ny]))
# # 	return visited


# def dfs(x,y,m):
# 	if m  == 0:
# 		return visited
# 	for i in range(4):
# 		nx = dx[i] + x
# 		ny = dy[i] + y

# 		if 0<= nx < n and 0<= ny < n:
# 			if not visited[nx][ny]:
# 				visited[nx][ny] = visited[x][y] + 1
# 				if arr[nx][ny] == 1:
# 					visited[nx][ny] = min(visited[nx][ny], visited[x][y])



# 	print(x,y,m)

# for i in range(n):
# 	for j in range(n):
# 		if arr[i][j] == 2:
# 			visited = [[0] * n for _ in range(n)]
# 			visited[i][j] = 1
# 			# bfs(i,j)





# import sys
# input = sys.stdin.readline

# N,M = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(N)]
# answer  = float('inf')
# chicken = []
# house = []

# def dfs(cur,arr):
# 	global answer
# 	if len(arr)==M:
# 		result = 0
# 		for x,y in house:
# 			min_dist = float('inf')
# 			for ix,iy in arr:
# 				dist=abs(x-ix) + abs(y-iy)
# 				min_dist = min(dist,min_dist)
# 			result += min_dist
# 		answer = min(answer,result)
# 		return

# 	if cur == len(chicken):
# 		return
# 	dfs(cur+1,arr+[chicken[cur]])
# 	dfs(cur+1,arr)


# for i in range(N):
# 	for j in range(N):
# 		if arr[i][j] == 1:
# 			house.append((i,j))
# 		if arr[i][j] == 2:
# 			chicken.append((i,j))



# dfs(0,[])
# print(answer)




