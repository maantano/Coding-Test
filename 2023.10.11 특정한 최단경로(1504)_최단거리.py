# 방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다. 또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

# 세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라. 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

# 첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력한다.


# 4 6
# 1 2 3
# 2 3 3
# 3 4 1
# 1 3 5
# 2 4 5
# 1 4 4
# 2 3

import sys
import heapq

input = sys.stdin.readline
INF= int(1e9)
n,m = map(int,input().split())


g = [[] for _ in range(n+1)]


for i in range(m):
	a,b,c = map(int,input().split())
	g[a].append((b,c))
	g[b].append((a,c))

via1,via2 = map(int,input().split())
def dijkstra(start):
	q = []
	distance = [INF] * (n+1)
	heapq.heappush(q,(0,start))
	distance[start] = 0

	while q:
		dist,now = heapq.heappop(q)
		if distance[now] < dist:
			continue
		for node,leaf in g[now]:
			cost = dist + leaf
			if cost < distance[node]:
				distance[node] = cost
				heapq.heappush(q,(cost,node))

	return distance

original_distance = dijkstra(1)
via1_distance = dijkstra(via1)
via2_distance = dijkstra(via2)


v1_path = original_distance[via1] + via1_distance[via2] + via2_distance[n]
v2_path = original_distance[via2] + via2_distance[via1] + via1_distance[n]

result = min(v1_path, v2_path)
print(result if result < INF else -1)
