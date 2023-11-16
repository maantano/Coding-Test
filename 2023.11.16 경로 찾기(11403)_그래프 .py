import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
g = [[] for _ in range(n)]



def bfs(start):
	q = deque([start])
	visited = [0] * n

	while q:
		node = q.popleft()
		for i in g[node]:
			if not visited[i]:
				visited[i] = 1
				q.append(i)
	print(*visited)


for i in range(n):
	arr = list(map(int,input().split()))
	for j in range(n):
		if arr[j]:
			g[i].append(j)
for i in range(n):
	bfs(i)




# import sys
# input = sys.stdin.readline
# from collections import deque
# n = int(input())
# g = [list(map(int,input().split())) for _ in range(n)]
# visited = [[0] * n for _ in range(n)]


# def bfs(start):
# 	q = deque([start])
# 	chk = [0 for _ in range(n)]

# 	while q:
# 		now = q.popleft()
# 		for i in range(n):
# 			if not chk[i] and g[now][i] == 1:
# 				q.append(i)
# 				visited[start][i] = 1
# 				chk[i] = 1
# for i in range(0,n):
# 	bfs(i)

# for i in visited:
# 	print(*i)






# import sys
# input = sys.stdin.readline

# n = int(input())
# g = []
# for _ in range(n):
# 	g.append(list(map(int,input().split())))

# for k in range(n):
# 	for i in range(n):
# 		for j in range(n):
# 			if g[i][k] == 1 and g[k][j] == 1:
# 				g[i][j] = 1
# for i in range(n):
# 	print(*g[i])
