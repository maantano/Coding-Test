# 5
# 8
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 1 5
# import sys
# input = sys.stdin.readline
# n = int(input())
# m = int(input())

# INF = int(1e9)
# g = [[INF] * (n+1) for _ in range(n+1)]

# for i in range(1,n+1):
# 	for j in range(1,n+1):
# 		if i == j:
# 			g[i][j] = 0

# for i in range(m):
# 	a,b,c = map(int,input().split())
# 	g[a][b] = c

# start,end = map(int,input().split())
# for k in range(1,n+1):
# 	for i in range(1,n+1):
# 		for j in range(1,n+1):
# 			g[i][j] = min(g[i][j], g[i][k]+g[k][j])
# print(g[start][end])



import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


n = int(input())
m = int(input())



distance = [INF] * (n+1)
g = [[] for _ in range(n+1)]

for i in range(m):
	a,b,c = map(int,input().split())
	g[a].append((b,c))

start,end = map(int,input().split())

def dijkstra(start):
	q = []
	heapq.heappush(q,(0,start))
	distance[start] = 0

	while q:
		dist,now = heapq.heappop(q)
		if distance[now] <dist:
			continue
		for node,leaf in g[now]:
			cost = dist + leaf
			if cost < distance[node]:
				distance[node] = cost
				heapq.heappush(q,(cost,node))
dijkstra(start)
print(distance[end])




