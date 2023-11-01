

# from collections import deque

# visited = [[0]*m for _ in range(n)]

# def bt(x,y):
# 	q = deque([(x,y)])

# answer = []
# def bt(idx,smallList):
# 	if idx == k:
# 		print(sum(smallList))
# 		return

# def bt(idx,smallList):
# 	if idx == k:
# 		answer.append(sum(smallList))
# 		return
# 	for i in range(n):
# 		for j in range(m):
# 			# for h in range(4):
# 			# 	nx = i + dx[h]
# 			# 	ny = j + dy[h]

# 			# if 0 <= nx < n and 0 <= ny <m:
# 			print(visited)
# 			if not visited[i][j]:
# 				visited[i][j] = 1
# 				if i+1 < n:
# 					visited[i+1][j] = 1
# 				if i -1 > 0:
# 					visited[i-1][j] = 1
# 				if j + 1 < m:
# 					visited[i][j+1] = 1
# 				if j -1 > m:
# 					visited[i][j-1] = 1
# 				print('@@@@@@@@@@@@@@@@@@@@@')
# 				print(visited)
# 				bt(idx+1,smallList+[arr[i][j]])
# 				visited[i][j] = 0
# 				if i+1 < n:
# 					visited[i+1][j] = 0
# 				if i -1 > 0:
# 					visited[i-1][j] = 0
# 				if j + 1 < m:
# 					visited[i][j+1] = 0
# 				if j -1 > m:
# 					visited[i][j-1] = 0
# bt(0,[])
# print(answer)


import sys
input = sys.stdin.readline

n,m,k = map(int,input().split(' '))
arr = [list(map(int,input().split(' '))) for _ in range(n)]
visited=[[0] * m for i in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]


answer = -1000000

def bt(px,py,idx,sum):
	if idx == k:
		global answer
		if answer < sum:
			answer = sum
		return
	for x in range(px,n):
		for y in range(py if x == px else 0,m):
			if visited[x][y]:
				continue
			ok = True
			for i in range(4):
				nx = x + dx[i]
				ny = y + dy[i]
				if 0 <= nx < n and 0<= ny < m:
					if visited[nx][ny]:
						ok = False
			if ok:
				visited[x][y] = 1
				bt(x,y,idx+1,sum+arr[x][y])
				visited[x][y]= 0

bt(0,0,0,0)
print(answer)
