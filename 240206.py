# import sys
# input = sys.stdin.readline
# from collections import deque

# n,k = map(int,input().split())
# q = deque()
# q.append(n)
# visited = [-1]*100001
# visited[n] = 0

# while q:
# 	s = q.popleft()

# 	if s == k:
# 		print(visited[s])
# 		break
# 	if 0<= s-1 < 100001 and visited[s-1] == -1:
# 		visited[s-1] = visited[s] + 1
# 		q.append(s-1)
# 	if 0<= s*2 < 100001 and visited[s*2] == -1:
# 		visited[s*2] = visited[s]
# 		q.appendleft(s*2)
# 	if 0<= s+1 < 100001 and visited[s+1] == -1:
# 		visited[s+1] = visited[s] + 1
# 		q.append(s+1)




# import sys
# input = sys.stdin.readline
# from collections import deque

# danger = []
# death = []
# INF = int(1e9)

# n = int(input())
# for _ in range(n):
# 	x1,y1,x2,y2 = map(int,input().split())
# 	if x1 > x2:
# 		x1,x2 = x2,x1
# 	if y1 > y2:
# 		y1,y2 = y2,y1
# 	danger.append([x1,y1,x2,y2])
# n = int(input())
# for _ in range(n):
# 	x1,y1,x2,y2 = map(int,input().split())
# 	if x1 > x2:
# 		x1,x2 = x2,x1
# 	if y1 > y2:
# 		y1,y2 = y2,y1
# 	death.append([x1,y1,x2,y2])

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# import heapq

# def djikstra():
# 	distance = [[INF for _ in range(501)]  for _ in range(501)]
# 	distance[0][0] = 0
# 	hq = []
# 	heapq.heappush(hq,[0,0,0])

# 	while hq:
# 		cost,row,col = heapq.heappop(hq)
# 		if distance[row][col] < cost : continue

# 		for i in range(4):
# 			nx = row + dx[i]
# 			ny = col + dy[i]

# 			if 0 <= nx< 501 and 0 <= ny < 501:
# 				flag = False
# 				for x1,y1,x2,y2 in death:
# 					if x1 <= nx <= x2 and y1<= ny <= y2:
# 						flag = True
# 						break
# 				if flag: continue
# 				newCost = 0
# 				for x1,y1,x2,y2 in danger:
# 					if x1 <= nx <= x2 and y1<= ny <= y2:
# 						newCost += 1
# 						break
# 				if distance[nx][ny] > cost + newCost:
# 					distance[nx][ny] = cost + newCost
# 					heapq.heappush(hq,(cost + newCost,nx,ny))
# 	return distance[500][500]

# dist = djikstra()
# if dist == INF : print(-1)
# else: print(dist)



# from collections import deque
# import sys
# direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# danger = []
# death = []

# N = int(sys.stdin.readline())
# for _ in range(N):
# 	X1, Y1, X2, Y2 = map(int, sys.stdin.readline().split())
# 	danger.append((X1, Y1, X2, Y2))

# M = int(sys.stdin.readline())
# for _ in range(M):
# 	X1, Y1, X2, Y2 = map(int, sys.stdin.readline().split())
# 	death.append((X1, Y1, X2, Y2))

# graph = [[0] * 501 for _ in range(501)]

# for i in range(501):
# 	for j in range(501):
# 		# 위험 영역에 속한다면
# 		for a1, b1, a2, b2 in danger:
# 			if (min(a1, a2) <= i <= max(a1, a2)) and (min(b1, b2) <= j <= max(b1, b2)):
# 				graph[i][j] = 1
# 		# 죽음 영역에 속한다면
# 		for a1, b1, a2, b2 in death:
# 			if (min(a1, a2) <= i <= max(a1, a2)) and (min(b1, b2) <= j <= max(b1, b2)):
# 				graph[i][j] = 2


# answer = 0
# visit = [[False] * 501 for _ in range(501)]
# q = deque()
# # x좌표, y좌표, 깎인 생명
# q.append((0, 0, 0))
# visit[0][0] = True
# can_reach = False

# while q:
# 	x, y, minus_life = q.popleft()
# 	if x == 500 and y == 500:
# 		can_reach = True
# 		answer = minus_life
# 		break

# 	for d in direction:
# 		nx = x + d[0]
# 		ny = y + d[1]

# 		if 0 <= nx <= 500 and 0 <= ny <= 500 and not visit[nx][ny]:
# 			if graph[nx][ny] == 0:
# 				q.appendleft((nx, ny, minus_life))
# 				visit[nx][ny] = True
# 			elif graph[nx][ny] == 1:
# 				q.append((nx, ny, minus_life + 1))
# 				visit[nx][ny] = True

# if can_reach:
# 	print(answer)
# else:
# 	print(-1)


# 알고스팟
# https://www.acmicpc.net/problem/1261
# import sys
# input = sys.stdin.readline

# from collections import deque

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# n,m = map(int,input().split())
# g = [list(map(int,input().rstrip())) for _ in range(m)]
# visited = [[-1] * n for _ in range(m)]

# def bfs(x,y):
# 	q = deque([(x,y)])
# 	visited[0][0] = 0

# 	while q:
# 		x,y = q.popleft()

# 		for i in range(4):
# 			nx = x +dx[i]
# 			ny = y +dy[i]

# 			if 0<= nx < m and 0<= ny <n:
# 				if visited[nx][ny]== -1:
# 					if g[nx][ny]:
# 						visited[nx][ny] = visited[x][y]+ 1
# 						q.append((nx,ny))
# 					else:
# 						visited[nx][ny] = visited[x][y]
# 						q.appendleft((nx,ny))

# bfs(0,0)
# print(visited[m-1][n-1])

# 미로만들기
# https://www.acmicpc.net/problem/2665

# import sys
# input = sys.stdin.readline
# from collections import deque

# n = int(input())
# g = [list(map(int,input().rstrip())) for _ in range(n)]

# visited = [[-1] * n for _ in range(n)]


# q = deque([(0,0)])
# visited[0][0] = 0

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# while q:
# 	x,y = q.popleft()

# 	for i in range(4):
# 		nx = x + dx[i]
# 		ny = y + dy[i]

# 		if 0<= nx < n and 0<= ny < n:
# 			if visited[nx][ny] == -1:
# 				if g[nx][ny] == 0:
# 					visited[nx][ny] = visited[x][y] + 1
# 					q.append((nx,ny))
# 				else:
# 					visited[nx][ny] = visited[x][y]
# 					q.appendleft((nx,ny))
# print(visited[n-1][n-1])


# import sys
# input = sys.stdin.readline

# from collections import deque
# n,m = map(int,input().split())
# x1,y1,x2,y2 = map(int,input().split())
# g = [list(input().rstrip()) for _ in range(n)]
# visited = [[0] * m for _ in range(n)]

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def bfs(x,y):
# 	q = deque([(x,y)])
# 	visited[x][y] = 1

# 	while q:
# 		x,y = q.popleft()

# 		for i in range(4):
# 			nx = x + dx[i]
# 			ny = y + dy[i]
# 			if 0<= nx < n and 0<= ny < m:
# 				if not visited[nx][ny]:
# 					if g[nx][ny] == '1':
# 						visited[nx][ny] = visited[x][y] + 1
# 						q.append((nx,ny))
# 					if g[nx][ny] == '0':
# 						visited[nx][ny] = visited[x][y]
# 						q.appendleft((nx,ny))
# 					if g[nx][ny] == '#':
# 						visited[nx][ny] = visited[x][y]
# 						return

# bfs(x1-1,y1-1)
# print(visited[x2-1][y2-1])


# import sys
# from collections import deque
# input = sys.stdin.readline

# n,m = map(int,input().split())
# g = [list(map(int,input().rstrip())) for _ in range(n)]
# visited = [[0] * m for _ in range(n)]

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]


# def bfs(x,y):
# 	q = deque([(x,y)])
# 	visited[x][y] = 1

# 	while q:
# 		x,y = q.popleft()
# 		for i in range(4):
# 			nx = x + dx[i]
# 			ny = y + dy[i]
# 			if 0 <= nx < n and 0 <= ny < m:
# 				if not visited[nx][ny] and g[nx][ny]:
# 					visited[nx][ny] = visited[x][y] + 1
# 					q.append((nx,ny))

# bfs(0,0)
# print(visited[n-1][m-1])

# 보물 찾기 2
# https://www.acmicpc.net/problem/27978
# import heapq
# import sys
# input = sys.stdin.readline

# dix =  ((1, 0, 1), (-1, 0, 1), (0, 1, 0), (0, -1, 1), (1, 1, 0), (-1, 1, 0), (1, -1, 1), (-1, -1, 1))

# N, M = map(int, input().strip().split())
# pan, q, answer, flag = [], [], 0, False
# for i in range(N):
# 	temp = input().strip()

# 	for j in range(M):
# 		if temp[j] == "K":
# 			sx, sy = i, j

# 		elif temp[j] == "*":
# 			ex, ey = i, j

# 	pan.append(temp)

# visited = [[0 for _ in range(M)] for _ in range(N)]
# visited[sx][sy] = 1
# heapq.heappush(q, (0, sx, sy))

# while q:
# 	cnt, x, y = heapq.heappop(q)
# 	if (x, y) == (ex, ey):
# 		answer, flag = cnt, True
# 		break

# 	for dx, dy, fuel in dix:
# 		nx, ny = x + dx, y + dy
# 		if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and pan[nx][ny] != "#":
# 			visited[nx][ny] = 1
# 			heapq.heappush(q, (cnt+fuel, nx, ny))

# print(answer if flag else -1)

# 틀림, 우선순위 큐로 돌리고, 타겟 위치 오면 break
# import sys
# input = sys.stdin.readline
# from collections import deque
# # dx1 =[-1,1,0,0,1,1,-1,-1]
# # dy1 =[0,0,-1,1,-1,1,-1,1]
# dx1 =[-1,1,0,1,-1]
# dy1 =[0,0,-1,-1,-1]
# dx2 = [-1,0,1]
# dy2 = [1,1,1]

# n,m = map(int,input().split())
# g = [list(input().rstrip()) for _ in range(n)]
# INF = int(1e9)
# visited = [[INF] * m for _ in range(n)]


# # 배는 암초 위를 지나다닐 수 없다
# # . 바다
# # # 암초
# # * 보물
# # K 배

# tx ,ty = 0,0
# answer = 0
# def bfs(x,y):
# 	global answer
# 	q = deque([(x,y)])
# 	visited[x][y] = 0

# 	while q:
# 		x,y = q.popleft()
# 		if (x, y) == (tx, ty):
# 			answer = visited[x][y]
# 			break
# 		for i in range(5):
# 			nx = x + dx1[i]
# 			ny = y + dy1[i]

# 			if 0 <= nx < n and 0 <= ny < m:
# 				if visited[nx][ny] == INF and not g[nx][ny] == '#':
# 					visited[nx][ny] = min(visited[nx][ny],visited[x][y] + 1)
# 					q.append((nx,ny))

# 			for i in range(3):
# 				nx = x + dx2[i]
# 				ny = y + dy2[i]
# 				if 0 <= nx < n and 0 <= ny < m:
# 					if visited[nx][ny] == INF  and not g[nx][ny] == '#':
# 						visited[nx][ny] = min(visited[nx][ny],visited[x][y])
# 						q.appendleft((nx,ny))



# for i in range(n):
# 	for j in range(m):
# 		if g[i][j] == 'K':
# 			bfs(i,j)
# 		if g[i][j] == '*':
# 			tx = i
# 			ty = j
# print(answer)
# print(visited)
# print(visited[tx][ty])




# import sys
# input = sys.stdin.readline
# from itertools import permutations

# data = ['1','2','3','4','5','6','7','8','9']
# n = int(input())
# num = list(permutations(data,3))

# for _ in range(n):
# 	n,s,b = map(int,input().split())
# 	n = list(str(n))
# 	remove_cnt = 0
# 	for i in range(len(num)):
# 		strike = ball = 0
# 		i -= remove_cnt
# 		for j in range(3):
# 			if num[i][j] == n[j]:
# 				strike += 1
# 			elif n[j] in num[i]:
# 				ball += 1
# 		if (strike != s) or (ball != b):
# 			num.remove(num[i])
# 			remove_cnt+=1
# print(len(num))





# https://www.acmicpc.net/problem/2589

# import sys
# input = sys.stdin.readline
# from collections import deque

# n,m = map(int,input().split())
# g = [list(input().rstrip()) for _ in range(n)]



# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def bfs(x,y):
# 	q = deque([(x,y)])
# 	visited = [[0] * m for _ in range(n)]
# 	visited[x][y] = 1
# 	answer = 0
# 	while q:
# 		x,y = q.popleft()

# 		for i in range(4):
# 			nx = x + dx[i]
# 			ny = y + dy[i]
# 			if nx < 0 or nx >=n or ny <0 or ny >=m:
# 			if 0<= nx < n and 0<= ny < m:
# 				if not visited[nx][ny] and g[nx][ny] == 'L':
# 					visited[nx][ny] = visited[x][y] + 1
# 					answer = max(answer, visited[nx][ny])
# 					q.append((nx,ny))
# 	return answer - 1

# ans = -int(1e9)
# for i in range(n):
# 	for j in range(m):
# 		if g[i][j] == 'L':
# 			ans = max(ans,bfs(i,j))

# print(ans)


# 배열 돌리기 4
# https://www.acmicpc.net/problem/17406

# import sys
# input = sys.stdin.readline
# from itertools import permutations
# from copy import deepcopy
# n,m,k = map(int,input().split())
# g = [list(map(int,input().split())) for _ in range(n)]
# rcs = [list(map(int,input().split())) for _ in range(k)]

# ans = int(1e9)

# for p in permutations(rcs,k):
# 	copy_g = deepcopy(g)
# 	for r,c,s in p:
# 		r-=1
# 		c-=1
# 		for n in range(s,0,-1):
# 			tmp = copy_g[r-n][c+n]
# 			copy_g[r-n][c-n+1:c+n+1] = copy_g[r-n][c-n:c+n]
# 			for row in range(r-n,r+n):
# 				copy_g[row][c-n] = copy_g[row+1][c-n]
# 			copy_g[r+n][c-n:c+n] = copy_g[r+n][c-n+1:c+n+1]
# 			for row in range(r+n,r-n,-1):
# 				copy_g[row][c+n] = copy_g[row-1][c+n]
# 			copy_g[r-n+1][c+n] = tmp
# 	for row in copy_g:
# 		ans = min(ans ,sum(row))
# print(ans)


import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())
g = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [[INF] * n for _ in range(m)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(m):
	a,b,c = map(int,input().split())
	g[a].append((b,c))

start, end = map(int, input().split())
costs = [1e9 for _ in range(n+1)]
heap = []
costs[start] = 0
heapq.heappush(heap, [0, start])

while heap:
	cur_cost, cur_v = heapq.heappop(heap)
	if costs[cur_v] < cur_cost:
		continue

	for next_v,next_cost in g[cur_v]:
		sum_cost = cur_cost+next_cost
		if sum_cost >= costs[next_v]:
			continue
		costs[next_v] = sum_cost
		heapq.heappush(heap,[sum_cost,next_v])
print(costs[end])

# def djikstra():
# 	q = []
# 	heapq.heappush(q,(0,0,0))
# 	distance[0][0] = 0

# 	while q:
# 		dist,r,c = heapq.heappop(q)
# 		if distance[r][c] < dist:
# 			continue
# 		for i in range(4):
# 			nr = r + dx[i]
# 			nc = c + dy[i]

# 			if nr < 0 or nr >= m or nc < 0 or nc >=n:
# 				continue

# 			if dist+g[nr][nc] < distance[nr][nc]:
# 				distance[nr][nc] = dist+g[nr][nc]
# 				heapq.heappush(q,(distance[nr][nc],nr,nc))

# djikstra()
# print(distance[m-1][n-1])









