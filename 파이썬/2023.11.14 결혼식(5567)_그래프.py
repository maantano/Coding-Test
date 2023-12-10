

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]

for i in range(m):
	a,b = map(int,input().split())
	arr[a].append(b)
	arr[b].append(a)

visited = [0] *(n+1)
visited[1] = 1
answer = []
def dfs(start,depth):
	if depth == 2:
		return
	for i in arr[start]:
		if not visited[i]:
			answer.append(i)
			dfs(i,depth+1)
dfs(1,0)
print(len(set(answer)))
