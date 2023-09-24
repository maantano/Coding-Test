n = int(input())
x,y = map(int,input().split())
m = int(input())
g = [[] for _ in range(n+1)]
for i in range(1,m+1):
	parent, son = map(int,input().split())
	g[parent].append(son)
	g[son].append(parent)

result = []
visited = [False] * (n+1)

def dfs(x,num):
	num += 1
	visited[x] = True
	if x == y:
		result.append(num)

	for i in g[x]:
		if not visited[i]:
			dfs(i,num)
dfs(x,0)
if len(result) == 0:
	print(-1)
else:
	print(result[0]-1)






