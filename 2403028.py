# import sys
# input = sys.stdin.readline
# from collections import deque
# n,m = map(int,input().split())

# g = [list(input()) for _ in range(m)]


# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def bfs(x,y,chk):
# 	cnt = 1
# 	q = deque([(x,y)])
# 	g[x][y] = -1
# 	while q:
# 		x,y = q.popleft()
# 		for i in range(4):
# 			nx = dx[i] + x
# 			ny = dy[i] + y
# 			if 0<= nx < m and 0<= ny < n:
# 				if g[nx][ny] == chk:
# 					g[nx][ny] = -1
# 					q.append((nx,ny))
# 					cnt+=1

# 	return cnt*cnt
# w,b=0,0
# for i in range(m):
# 	for j in range(n):
# 		if g[i][j] == 'B':
# 			b += bfs(i,j,'B')
# 		elif g[i][j] == 'W':
# 			w += bfs(i,j,'W')
# print(w,b,sep=' ')

# 컴백홈
# https://www.acmicpc.net/problem/1189
# import sys
# input = sys.stdin.readline
# r,c,k = map(int,input().split())
# g = [list(input()) for _ in range(r)]
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# ans = 0
# def dfs(x,y,cnt):
# 	global ans
# 	g[x][y] = 'T'
# 	if x == 0 and y == c-1:
# 		if cnt == k:
# 			ans+=1
# 		return
# 	for i in range(4):
# 		nx = dx[i] + x
# 		ny = dy[i] + y

# 		if 0<=nx<r and 0<= ny <c:
# 			if g[nx][ny] != 'T':
# 				g[nx][ny] ='T'
# 				dfs(nx,ny,cnt+1)
# 				g[nx][ny] ='.'

# dfs(r-1,0,1)
# print(ans)

# 숫자고르기
# https://www.acmicpc.net/problem/2668
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# n = int(input())
# g = [[] for _ in range(n+1)]

# for i in range(1,n+1):
# 	g[i].append(int(input()))

# def dfs(num):

# 	if not visited[num]:
# 		visited[num] = 1
# 		for i in g[num]:
# 			a.add(num)
# 			b.add(i)
# 			if a == b:
# 				ans.extend(list(b))
# 				return
# 			dfs(i)
# 	visited[num] = 0

# ans = []
# for i in range(1,n+1):
# 	visited = [0] * (n+1)
# 	a = set()
# 	b = set()
# 	dfs(i)
# ans = list(set(ans))
# print(len(ans))
# for i in sorted(ans):
# 	print(i)

# 트리와 쿼리
# https://www.acmicpc.net/problem/15681
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**9)
# n,r,q = map(int,input().split())
# g = [[] for _ in range(n+1)]
# visited = [0] * (n+1)
# for i in range(n-1):
# 	u,v = map(int,input().split())
# 	g[u].append(v)
# 	g[v].append(u)

# def dfs(num):
# 	visited[num] = 1
# 	for i in g[num]:
# 		if not visited[i]:
# 			dfs(i)
# 			visited[num] += visited[i]

# dfs(r)

# for i in range(q):
# 	u = int(input())
# 	print(visited[u])


# 이분 그래프
# https://www.acmicpc.net/problem/1707

# def dfs(num,chk):
# 	# print(visited,chk)
# 	if not visited[num][0]:
# 		if visited[num][1] == chk:
# 			return 'NO'
# 		for i in g[num]:
# 			visited[num][1] = chk % 2
# 			dfs(i,chk+1)
# 	return 'YES'



# k = int(input())
# for _ in range(k):
# 	v,e = map(int,input().split())
# 	g = [[] for _ in range(v+1)]
# 	visited = [[0,0] for _ in range(v+1)]

# 	for i in range(e):
# 		a,b = map(int,input().split())
# 		g[a].append(b)
# 		g[b].append(a)

# 	print(dfs(1,1))

# def dfs(num,chk):
# 	visited[num] = chk

# 	for i in g[num]:
# 		if not visited[i]:
# 			a = dfs(i,-chk)
# 			if not a:
# 				return False
# 		elif visited[i] == visited[num]:
# 			return False
# 	return True



# k = int(input())
# for _ in range(k):
# 	v,e = map(int,input().split())
# 	g = [[] for _ in range(v+1)]
# 	visited = [0] * (v+1)

# 	for i in range(e):
# 		a,b = map(int,input().split())
# 		g[a].append(b)
# 		g[b].append(a)

# 	for i in range(1,v+1):
# 		if not visited[i]:
# 			result = dfs(i,1)
# 			if not result:
# 				break
# 	print('YES' if result else 'NO')



# import sys
# input = sys.stdin.readline
# from collections import deque

# def sol():
# 	for _ in range(k):
# 		V,E = map(int,input().split())
# 		g = [[] for _ in range(V+1)]
# 		for i in range(E):
# 			u,v = map(int,input().split())
# 			g[u].append(v)
# 			g[v].append(u)

# 		visited = [0] * (V+1)

# 		for i in range(1,V+1):
# 			if visited[i]:
# 				continue
# 			visited[i] = 1

# 			q = deque([i])
# 			while q:
# 				now = q.popleft()
# 				nextVisited = visited[now] % 2 +1

# 				for next in g[now]:
# 					if not visited[next]:
# 						visited[next] = nextVisited
# 						q.append(next)
# 					elif visited[next] != nextVisited:
# 						return 'NO'
# 		return 'YES'

# 노드사이의 거리
# https://www.acmicpc.net/problem/1240

# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# g = [[] for _ in range(n+1)]

# def dfs(start,end,chk):
# 	global cnt
# 	if start == end:
# 		cnt = chk
# 		return

# 	for i,j in g[start]:
# 		if not visited[i]:
# 			visited[i] = 1
# 			dfs(i,end,chk+j)


# for i in range(n-1):
# 	a,b,c = map(int,input().split())
# 	g[a].append([b,c])
# 	g[b].append([a,c])


# for i in range(m):
# 	x,y = map(int,input().split())
# 	cnt = 0
# 	visited = [0] * (n+1)
# 	visited[x] = 1
# 	dfs(x,y,0)
# 	print(cnt)


# 구슬 찾기
# https://www.acmicpc.net/problem/2617

# n,m = map(int,input().split())

# hl = [[] for _ in range(n+1)]
# ll = [[] for _ in range(n+1)]

# for i in range(m):
# 	heavy,light = map(int,input().split())
# 	hl[heavy].append(light)
# 	ll[light].append(heavy)


# def dfs(l,v):
# 	ans = 0
# 	for node in l[v]:
# 		if not visited[node]:
# 			visited[node] = 1
# 			ans+=1
# 			ans += dfs(l,node)
# 	return ans

# mid = (n+1) // 2
# res = 0

# for v in range(1,n+1):
# 	visited = [0] * (n+1)
# 	if dfs(hl,v) >= mid:
# 		res+=1
# 	if dfs(ll,v) >= mid:
# 		res+=1
# print(res)

# 회사 문화 1
# https://www.acmicpc.net/problem/14267


