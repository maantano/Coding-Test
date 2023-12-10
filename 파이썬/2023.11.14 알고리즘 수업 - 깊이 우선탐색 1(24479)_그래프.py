import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n,m,c = map(int,input().split())
arr = [[] for _ in range(n+1)]
for i in range(m):
	a,b = map(int,input().split())
	arr[a].append(b)
	arr[b].append(a)

visited = [0] * (n+1)
visited[c] = 1

for i in range(n):
	arr[i].sort()

def dfs(start):
	for i in arr[start]:
		if not visited[i]:
			visited[i] = visited[start]+1
			dfs(i)

dfs(c)
for i in visited[1:]:
	print(i)




# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 9)

# n,m,c = map(int,input().split())
# arr = [[] for _ in range(n+1)]

# for i in range(m):
# 	a,b = map(int,input().split())
# 	arr[a].append(b)
# 	arr[b].append(a)

# visited = [0] * (n+1)
# cnt = 1

# def dfs(start):
# 	global cnt
# 	visited[start] = cnt
# 	arr[start].sort()
# 	for i in arr[start]:
# 		if not visited[i]:
# 			cnt+=1
# 			dfs(i)

# dfs(c)
# for i in range(1,n+1):
# 	print(visited[i])


