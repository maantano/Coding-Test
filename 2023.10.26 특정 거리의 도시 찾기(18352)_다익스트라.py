import sys
input = sys.stdin.readline

n,m,k,start = map(int,input().split())
arr = [[] for _ in range(n+1)]
for i in range(m):
	a,b = map(int,input().split())
	arr[a].append((b,1))
import heapq
INF = int(1e9)
distance = [INF] * (n+1)

def dijkstra(start):
	q = []
	heapq.heappush(q,(0,start))
	distance[start] = 0

	while q:
		dist,now = heapq.heappop(q)
		if distance[now] < dist:
			continue
		for node,leaf in arr[now]:
			cost = dist+leaf
			if cost < distance[node]:
				distance[node] = cost
				heapq.heappush(q,(cost,node))


dijkstra(start)

answer = []
for i in range(1,n+1):
	if distance[i] == k: answer.append(i)
if len(answer) == 0: print(-1)
else:
	for i in answer : print(i , end = '\n')
