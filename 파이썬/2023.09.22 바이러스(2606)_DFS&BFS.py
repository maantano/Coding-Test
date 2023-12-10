
# n = 7
# m = 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7

#  DFS ========================================
n = int(input())
m = int(input())

g = [[] for _ in range(n+1)]
for i in range(m):
	x,y = map(int,input().split())
	g[x].append(y)
	g[y].append(x)

for j in g:
	j.sort()

stack = []
chk = [False] * (n+1)
def dfs(v):
	chk[v] = True
	for i in g[v]:
		if chk[i] == False:
			chk[i] = True
			stack.append(i)
			dfs(i)

dfs(1)
print(len(stack))


#  BFS ========================================
n = int(input())
m = int(input())

g = [[] for _ in range(n+1)]
for i in range(m):
	x,y = map(int,input().split())
	g[x].append(y)
	g[y].append(x)

for j in g:
	j.sort()

from collections import deque
bfsChk = [False] * (n+1)

def bfs(v):
	count = 0
	q = deque([v])
	bfsChk[v] = True
	while q:
		start = q.popleft()
		for i in g[start]:
			if bfsChk[i] == False:
				bfsChk[i] = True
				q.append(i)
				count+=1
	print(count)
bfs(1)






