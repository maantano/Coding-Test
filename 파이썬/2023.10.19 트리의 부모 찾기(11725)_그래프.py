import sys
input = sys.stdin.readline

n = int(input())

arr = [[] for _ in range(n+1)]


for i in range(n-1):
	x,y = map(int,input().split())
	arr[y].append(x)
	arr[x].append(y)

visited = [0]*(n+1)


answer = []

def dfs(s):
	for i in arr[s]:
		if not visited[i]:
			visited[i] = s
			dfs(i)
dfs(1)

for i in range(2,n+1):
	print(visited[i])


# import sys
# from collections import deque

# N = int(sys.stdin.readline())
# graph = [[] for i in range(N+1)]
# for _ in range(N-1):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)

# queue = deque()
# queue.append(1)

# ans = [0]*(N+1)

# def bfs():
#     while queue:
#         now = queue.popleft()
#         for nxt in graph[now]:
#             if ans[nxt] == 0:
#                 ans[nxt] = now
#                 queue.append(nxt)

# bfs()
# res = ans[2:]
# for x in res:
#     print(x)
