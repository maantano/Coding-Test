import sys
input = sys.stdin.readline

n,m = map(int,input().split())

INF = int(1e9)
arr = [[INF] * (n+1) for i in range(n+1)]

for a in range(1,n+1):
	for b in range(1,n+1):
		if a == b:
			arr[a][b] = 0

for _ in range(m):
	a,b = map(int,input().split())
	arr[a][b]=1
	arr[b][a]=1

for k in range(1,n+1):
	for a in range(1,n+1):
		for b in range(1,n+1):
			arr[a][b] = min (arr[a][b],arr[a][k]+arr[k][b])

answer = 0
b = INF

for i in range(n,0,-1):
	s = sum(arr[i][1:])
	if b >= s:
		b = s
		answer = i

print(answer)


# import sys
# input = sys.stdin.readline
# from collections import deque


# def bfs(x):
# 	q = deque([(x)])
# 	visited[x] = 1

# 	while q:
# 		x = q.popleft()

# 		for i in arr[x]:
# 			if not visited[i]:
# 				visited[i] = visited[x] + 1
# 				q.append(i)



# n,m = map(int,input().split())
# arr = [[] for _ in range(n+1)]

# for i in range(m):
# 	a,b = map(int,input().split())
# 	arr[a].append(b)
# 	arr[b].append(a)

# res = []
# for i in range(1,n+1):
# 	visited = [0] * (n+1)
# 	bfs(i)
# 	res.append(sum(visited))

# print(res.index(min(res))+1)



