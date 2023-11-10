import sys
input = sys.stdin.readline
n,m = map(int,input().split())

INF = int(1e9)

distance = [INF] * (n+1)
arr = [[] for _ in range(n+1)]

for _ in range(m):
	a,b,c =map(int,input().split())
	arr[a].append((b,c))
	arr[b].append((a,c))

import heapq
def dijkstra(start):
	q = []
	heapq.heappush(q,(0,start))
	distance[start] = 0

	while q:
		dist,now = heapq.heappop(q)
		if distance[now] < dist:
			continue
		for node,leaf in arr[now]:
			cost = leaf + dist
			if cost < distance[node]:
				distance[node] = cost
				heapq.heappush(q,(cost,node))

dijkstra(1)
print(distance[n])

