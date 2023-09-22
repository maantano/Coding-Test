n,m,v = map(int,input().split())

g = [[]*m for _ in range(n+1)]
for i in range(m):
	x,y = map(int,input().split())
	g[x].append(y)
	g[y].append(x) # 이게 키!!

for i in g:
	i.sort()

def dfs(v):
	chk[v] = True
	print(v,end=' ')
	for i in g[v]:
		if not chk[i]:
			dfs(i)
chk = [False] * (n+1)
dfs(v)



from collections import deque

def bfs(v):
	q = deque([v])
	chk[v] = True
	while q:
		start = q.popleft()
		print(start,end =' ')
		for i in g[start]:
			if chk[i] == False:
				q.append(i)
				chk[i] = True

chk = [False] * (n+1)
print()
bfs(v)
