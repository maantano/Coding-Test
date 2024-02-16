# 숨바꼭질
# https://www.acmicpc.net/problem/1697
import sys
input = sys.stdin.readline


# from collections import deque
# n,k = map(int,input().split())
# MAX = 100001
# dp = [0] * (MAX)

# def bfs(start):
# 	q = deque([(start)])
# 	while q:
# 		chk = q.popleft()
# 		if chk == k:
# 			return dp[chk]
# 		for i in (chk-1,chk+1,chk*2):
# 			if 0<=i< MAX and not dp[i]:
# 				dp[i] = dp[chk] + 1
# 				q.append(i)
# print(bfs(n))

sys.setrecursionlimit(10**6)
n,m = map(int,input().split())
g = [[] for _ in range(n+1)]

for i in range(m):
	u,v = map(int,input().split())
	g[u].append(v)
	g[v].append(u)

from collections import deque
visited = [0] * (n+1)
def bfs(start,visited,g):
	q = deque([start])
	visited[start] = 1

	while q:
		v = q.popleft()
		for i in g[v]:
			if not visited[i]:
				visited[i] = 1
				q.append(i)
cnt = 0

for i in range(1,n+1):
	if not visited[i]:
		bfs(i,visited,g)
		cnt+=1

print(cnt)






