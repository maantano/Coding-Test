# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = []
# for i in range(n):
# 	arr.append(list(map(int,input().split())))

# visited = [0] * (n+1)
# p = []
# def tsp(start,answer,idx):

# 	if idx == n:
# 		p.append(answer)
# 		return

# 	for j in range(n):
# 		if j == start:
# 			continue
# 		if 	not visited[j]:
# 			visited[j] = 1
# 			answer += arr[start][j]
# 			tsp(j,answer,idx+1)
# 			visited[j] = 0
# 			answer -= arr[start][j]
# tsp(0,0,0)


# print(min(p))

import sys
input = sys.stdin.readline

n = int(input())
l = [list(map(int,input().split())) for _ in range(n)]
visited = [0] * n
m = int(1e9)

def dfs(depth,start,cost):
	global m
	if depth == n-1 and l[start][0] !=0:
		m = min(m,cost+l[start][0])
		return
	for i in range(n):
		if not visited[i] and l[start][i] != 0:
			visited[i] = 1
			dfs(depth+1,i,cost + l[start][i])
			visited[i] = 0


visited[0] = 1
dfs(0,0,0)
print(m)
