# # 치킨배달
# https://www.acmicpc.net/problem/15686

# n,m = map(int,input().split())

# arr = [list(map(int,input().split())) for _ in range(n)]

# chicken = []
# house = []

# answer = int(1e9)

# for i in range(n):
# 	for j in range(n):
# 		if arr[i][j] == 1:
# 			house.append((i,j))
# 		if arr[i][j] == 2:
# 			chicken.append((i,j))
# import math
# def dfs(cur,arr):
# 	global answer
# 	if (len(arr)) == m:
# 		result = 0
# 		for x,y in house:
# 			min_dist = int(1e9)
# 			for ix,iy in arr:
# 				dist = abs(x-ix)+abs(y-iy)
# 				min_dist = min(min_dist,dist)
# 			result += min_dist
# 		answer = min(answer,result)
# 		return
# 	if cur == len(chicken):
# 		return
# 	dfs(cur+1,arr+[chicken[cur]])
# 	dfs(cur+1,arr)

# dfs(0,[])
# print(answer)

# 나머지 합
# https://www.acmicpc.net/problem/10986
# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# arr = list(map(int,input().split()))
# dp = [0] * m
# sum = 0

# for i in range(n):
# 	sum += arr[i]
# 	dp[sum%m] += 1

# result = dp[0]

# for i in dp:
# 	result += (i * (i-1)) // 2
# print(result)


# 1 : ->
# 2 : <->
# 3 : ^| ->
# 4 : < ^| ->
# 5 : 상하좌우

# 1. 구십도 회전
# 2. 6을 만나면 스탑

import copy
n, m = map(int, input().split())
cctv = []
graph = []
mode = [
	[],
	[[0], [1], [2], [3]],
	[[0, 2], [1, 3]],
	[[0, 1], [1, 2], [2, 3], [0, 3]],
	[[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
	[[0, 1, 2, 3]],
]

# 북 - 동 - 남 - 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
	data = list(map(int, input().split()))
	graph.append(data)
	for j in range(m):
		if data[j] in [1, 2, 3, 4, 5]:
			cctv.append([data[j], i, j])

def fill(board, mm, x, y):
	for i in mm:
		nx = x
		ny = y
		while True:
			nx += dx[i]
			ny += dy[i]
			if nx < 0 or ny < 0 or nx >= n or ny >= m:
				break
			if board[nx][ny] == 6:
				break
			elif board[nx][ny] == 0:
				board[nx][ny] = 7

def dfs(depth, arr):
	global min_value
	if depth == len(cctv):
		count = 0
		for i in range(n):
			count += arr[i].count(0)
		min_value = min(min_value, count)
		return
	temp = copy.deepcopy(arr)
	cctv_num, x, y = cctv[depth]
	for i in mode[cctv_num]:
		fill(temp, i, x, y)
		dfs(depth+1, temp)
		temp = copy.deepcopy(arr)

min_value = int(1e9)
dfs(0, graph)
print(min_value)
