# # n(1≤n≤1,000)개의 도시가 있다.
# # 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1≤m≤100,000)개의 버스가 있다.
# # 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다.
# # 그러면 A번째 도시에서 B번째 도시 까지 가는데 드는 최소비용과 경로를 출력하여라.
# # 항상 시작점에서 도착점으로의 경로가 존재한다.

# # 첫째 줄에 도시의 개수 n(1≤n≤1,000)이 주어지고 둘째 줄에는 버스의 개수 m(1≤m≤100,000)이 주어진다.
# # 그리고 셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다.
# # 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다.


# # 첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.

# # 둘째 줄에는 그러한 최소 비용을 갖는 경로에 포함되어있는 도시의 개수를 출력한다. 출발 도시와 도착 도시도 포함한다.

# # 셋째 줄에는 최소 비용을 갖는 경로를 방문하는 도시 순서대로 출력한다.



import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


n = int(input())
m = int(input())

g = [[] for _ in range(n+1)]
distance = [INF] * (n+1)


for i in range(m):
	a,b,c = map(int,input().split())
	g[a].append((b,c))

start,end = map(int,input().split())
nearnest = [start] * (n + 1)

def dijkstra(start):
	q = []
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
				nearnest[node] = now
				heapq.heappush(q,(cost,node))
dijkstra(start)


path = [end]
now = end
while now != start:
	now = nearnest[now]
	path.append(now)
path.reverse()


print(distance[end])
print(len(path))

print(' '.join(map(str,path)))



# import sys, heapq
# input = sys.stdin.readline

# n = int(input())
# m = int(input())
# graph = [[] for _ in range(n + 1)]

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))

# start, end = map(int, input().split())

# # 가장 가까운 노드를 기록
# nearnest = [start] * (n + 1)
# distance = [1e9] * (n + 1)

# q = [(0, start)]
# while q:
#     dist, now = heapq.heappop(q)
#     if dist > distance[now]:
#         continue

#     for next, nextDist in graph[now]:
#         cost = nextDist + dist
#         if cost < distance[next]:
#             distance[next], nearnest[next] = cost, now
#             heapq.heappush(q, (cost, next))

# ans = []
# tmp = end
# while tmp != start:
#     ans.append(str(tmp))
#     tmp = nearnest[tmp]

# ans.append(str(start))
# ans.reverse()

# print(distance[end])
# print(len(ans))
# print(" ".join(ans))
