import sys
input = sys.stdin.readline
import heapq


n,m,r  = map(int,input().split())
t = [0]+list(map(int,input().split()))
arr = [[] for _ in range(n+1)]

for i in range(r):
	a,b,c = map(int,input().split())
	arr[a].append((b,c))
	arr[b].append((a,c))


def dijkstra(start):
	q = []
	heapq.heappush(q,(0,start))
	distance[start] = 0

	while q:
		dist,now= heapq.heappop(q)
		if distance[now] < dist:
			continue

		for node,leaf in arr[now]:
			cost = dist + leaf
			if  cost < distance[node]:
				distance[node] = cost
				heapq.heappush(q,(cost,node))



ans = 0
INF = int(1e9)
for i in range(1,n+1):
	distance = [INF] * (n+1)
	dijkstra(i)
	tmp = 0
	for d in range(1,n+1):
		if m >= distance[d]:
			tmp += t[d]
	ans = max(ans,tmp)
print(ans)

