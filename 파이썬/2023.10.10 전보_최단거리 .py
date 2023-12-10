# 다익스트라

# INPUT
# 3 2 1
# 1 2 4
# 1 3 2

# OUTPUT
# 2 4

import sys
import heapq


input = sys.stdin.readline
INF = int(1e9)

n,m,start = map(int,input().split())
g = [[] for i in range(n+1)]
distance = [INF] * (n+1)


for i in range(m):
	x,y,z = map(int,input().split())
	g[x].append((y,z))



def dijkstra(start):
	q = []
	heapq.heappush(q,(0,start))
	distance[start] = 0


	while q:
		dist,now = heapq.heappop(q)

		if distance[now] < dist:
			continue
		for i in g[now]:
			cost = dist + i[1]
			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(q,(cost,i[0]))

dijkstra(start)

count = 0
maxDistacne = 0
for d in distance:
	if d != INF:
		count+=1
		maxDistacne = max(maxDistacne,d)

print(count-1,maxDistacne)


