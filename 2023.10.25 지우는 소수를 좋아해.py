import sys
input = sys.stdin.readline
n,d = map(int,input().split())

# 출발위치, 도착위치, 지름길 길이
import heapq

arr = [[] for _ in range(d+1)]
INF = int(1e9)
distance = [INF] * (d+1)

for i in range(d):
	arr[i].append((i+1,1))

for _ in range(n):
	a,b,c = map(int,input().split())
	if b > d:
		continue
	arr[a].append((b,c))



def dijkstra(start):
	q = []
	heapq.heappush(q,(0,start))
	distance[0] = 0
	while q:
		dist,now = heapq.heappop(q)
		if distance[now] < dist:
			continue
		for node,leaf in arr[now]:
			cost = dist + leaf
			if cost < distance[node]:
				distance[node] = cost
				heapq.heappush(q,(cost,node))

dijkstra(0)
print(distance)
