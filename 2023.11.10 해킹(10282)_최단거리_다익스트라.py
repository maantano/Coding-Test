import sys
from collections import deque
input = sys.stdin.readline



import heapq
def dijkstra(start):
	q = []
	heapq.heappush(q,(0,start))
	distance[start] = 0
	while q:
		dist,now= heapq.heappop(q)
		for node,leaf in arr[now]:
			cost = dist+leaf
			if cost < distance[node]:
				distance[node] = cost
				heapq.heappush(q,(cost,node))




INF = int(1e9)
t = int(input())
for _ in range(t):
	n,d,c = map(int,input().split())
	arr = [[] for _ in range(n+1)]
	distance = [INF] * (n+1)
	for i in range(d):
		a,b,s = map(int,input().split())
		arr[b].append((a,s))
	dijkstra(c)

	cnt = 0
	ans = 0
	for i in distance:
		if i != INF:
			cnt +=1
			ans = max(ans,i)
	print(f'{cnt} {ans}')
