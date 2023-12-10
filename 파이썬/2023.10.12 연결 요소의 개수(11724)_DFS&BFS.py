
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# def dfs(g,x,visited):
# 	visited[x] = 1
# 	for i in g[x]:
# 		if not visited[i]:
# 			dfs(g,i,visited)


# n,m = map(int,input().split())
# g = [[] for _ in range(n+1)]



# for i in range(m):
# 	a,b = map(int,input().split())
# 	g[a].append(b)
# 	g[b].append(a)

# # print(g)
# result = 0
# visited = [0] * (n+1)

# for i in range(1,n+1):
# 	if not visited[i]:
# 		dfs(g,i,visited)
# 		result+=1
# print(result)










from collections import deque

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def bfs(g,x,visited):
	q = deque([x])
	visited[x] = 1

	while q:
		x = q.popleft()
		for i in g[x]:
			if not visited[i]:
				visited[i] = 1
				q.append(i)




n,m = map(int,input().split())

g = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
	a,b = map(int,input().split())
	g[a].append(b)
	g[b].append(a)

result = 0
for i in range(1,n+1):
	if not visited[i]:
		bfs(g,i,visited)
		result+=1
print(result)
