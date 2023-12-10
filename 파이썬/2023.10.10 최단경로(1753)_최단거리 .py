import sys
import heapq

input = sys.stdin.readline

V,E = map(int,input().split())
start = int(input())

INF = int(1e9)
distance = [INF] * (V+1)

g = [[] for _ in range(V+1)]

for i in range(E):
	u,v,w = map(int,input().split())
	g[u].append((v,w))
def dijkstra(start):
	q = []
	heapq.heappush(q,(0,start))
	distance[start] = 0

	while q:
		dist,now = heapq.heappop(q)
		if distance[now] < dist:
			continue

	#  중요!!!!!!!
	#  g에는  (도착지, 거리) 이렇게  넣었고
	#  큐에는 (거리,도착지) 이렇게 넣었다.
	# 우선순위 큐에서는 첫번째 요소로 정렬 하기 때문에!!!
	#  중요!!!!!!!
		for i in g[now]:
			cost = i[1] + dist
			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(q,(cost,i[0]))

dijkstra(start)
for i in range(1,V+1):
	if distance[i] == INF:
		print('INF')
	else:
		print(distance[i])



