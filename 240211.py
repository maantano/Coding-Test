
# 바이러스
# https://www.acmicpc.net/problem/2606

# v = int(input())
# e = int(input())
# graph = [[] for _ in range(v+1)]
# for _ in range(e):
# 	a, b = map(int, input().split())
# 	graph[a].append(b)
# 	graph[b].append(a)

# def dfs(x):
# 	global count
# 	visited[x] = True
# 	count += 1
# 	for node in graph[x]:
# 		if visited[node]:
# 			continue
# 		dfs(node)

# count = 0
# visited = [False for _ in range(v+1)]
# dfs(1)
# print(count-1)


# from collections import deque

# v = int(input())
# e = int(input())
# graph = [[] for _ in range(v+1)]
# for _ in range(e):
# 	a, b = map(int, input().split())
# 	graph[a].append(b)
# 	graph[b].append(a)


# def bfs(x):
# 	deq = deque([x])
# 	count = 0
# 	visited[x] = True
# 	while deq:
# 		node = deq.popleft()
# 		for next_node in graph[node]:
# 			if not visited[next_node]:
# 				visited[next_node] = True
# 				deq.append(next_node)
# 				count += 1

# 	return count

# visited = [False for _ in range(v+1)]
# print(bfs(1))

# 단지번호붙이기
# https://www.acmicpc.net/problem/2667

# from collections import deque
# n = int(input())

# g = [list(map(int,input())) for _ in range(n)]
# visited = [[0] * n for _ in range(n)]
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def bfs(x,y):
# 	q = deque([(x,y)])
# 	visited[x][y] = 1
# 	cnt = 1

# 	while q:
# 		x,y = q.popleft()

# 		for i in range(4):
# 			nx = dx[i] + x
# 			ny = dy[i] + y

# 			if 0 <= nx < n and 0<= ny < n:
# 				if not visited[nx][ny] and g[nx][ny]:
# 					visited[nx][ny] = 1
# 					cnt+=1
# 					q.append((nx,ny))
# 	return cnt
# answer = []
# for i in range(n):
# 	for j in range(n):
# 		if g[i][j]>0 and not visited[i][j]:
# 			answer.append(bfs(i,j))
# print(len(answer))
# for a in sorted(answer):
# 	print(a)


from collections import deque


# def dfs(start):
# 	visited[start] = True
# 	print(start, end=" ")

# 	for i in graph[start]:
# 		if not visited[i]:
# 			dfs(i)


# def bfs(start):
# 	queue = deque([start])
# 	visited[start] = True
# 	while queue:

# 		v = queue.popleft()
# 		print(v, end=" ")
# 		for i in graph[v]:
# 			if not visited[i]:
# 				visited[i] = True
# 				queue.append(i)


# N, M, V = map(int, input().split())
# graph = [[] for _ in range(N + 1)]

# for _ in range(M):
# 	a, b = map(int, input().split())
# 	graph[a].append(b)
# 	graph[b].append(a)

# # 정렬
# for i in graph:
# 	i.sort()

# # dfs
# visited = [False] * (N + 1)
# dfs(V)
# print()

# # bfs
# visited = [False] * (N + 1)
# bfs(V)


# 합 구하기
# https://www.acmicpc.net/problem/11441


# 메모리 초과

# n = int(input())
# arr = list(map(int,input().split()))

# visited = [[0] * n for _ in range(n)]

# for i in range(n):
# 	for j in range(i+1):
# 		visited[i][j] = arr[i] + visited[i-1][j]

# m = int(input())
# for i in range(m):
# 	a,b = map(int,input().split())
# 	print(visited[b-1][a-1])

# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int,input().split()))
# ans  = [0] *(n+1)
# for i in range(1,n+1):
# 	ans[i] = arr[i-1]+ans[i-1]
# print(ans)
# m = int(input())
# for _ in range(m):
# 	a,b = map(int,input().split())
# 	print(ans[n]-ans[i-1])



# 블로그
# https://www.acmicpc.net/problem/21921


# n,x = map(int,input().split())
# arr = list(map(int,input().split()))


# if not max(arr):
# 	print('SAD')
# else:
# 	value = sum(arr[:x])
# 	max_v = value
# 	max_cnt = 1

# 	for i in range(x,n):
# 		value += arr[i]
# 		value -= arr[i-x]

# 		if value > max_v:
# 			max_v = value
# 			max_cnt = 1
# 		elif value == max_v:
# 			max_cnt +=1

# 	print(max_v)
# 	print(max_cnt)


# 인간-컴퓨터 상호작용
# https://www.acmicpc.net/problem/16139


# S = input().rstrip()
# q = int(input())

# import sys

# input = sys.stdin.readline

# name = input().strip()
# n = int(input())
# arr = [[0 for i in range(26)] for i in range(len(name))]
# arr[0][ord(name[0]) - 97] = 1
# for i in range(1, len(name)):
# 	arr[i][ord(name[i]) - 97] = 1
# 	for j in range(26):
# 		arr[i][j] += arr[i - 1][j]
# print(arr)

# 직사각형
# https://www.acmicpc.net/problem/2527

for _ in range(4):
	x1,y1,p1,q1,x2,y2,p2,q2 = map(int,input().split())
	print(x1,y1,p1,q1,x2,y2,p2,q1)
	if p1 < x2 or p2 < x1 or y1 > q2 or q1 < y2:
			print('d')
			continue
	elif x1==p2 or x2==p1:
		# case (c)
		if q1==y2 or q2==y1:
			print('c')
			continue
		# case (b)
		else:
			print('b')
			continue
	elif q1==y2 or q2==y1:
		print('b')
		continue

	# case (a)
	else:
		print('a')
		continue
