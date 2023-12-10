import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n+1)]


for _ in range(n-1):
	a,b,c = map(int,input().split())
	arr[a].append([b,c])
	arr[b].append([a,c])

def dfs(start,d):
	for node,leaf in arr[start]:
		if visited[node] == -1:
			visited[node] = d + leaf
			dfs(node,d + leaf)

visited = [-1] * (n+1)
visited[1] = 0
dfs(1,0)

start = visited.index(max(visited))
visited = [-1] * (n+1)
visited[start] = 0
dfs(start,0)

print(max(visited))
