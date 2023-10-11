# 4 8 2
# 1 2 4
# 1 3 2
# 1 4 7
# 2 1 1
# 2 3 5
# 3 1 2
# 3 4 4
# 4 2 3

# 시간 초과
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# n,m,x = map(int,input().split())
# g = [[INF]*(n+1) for _ in range(n+1)]

# for i in range(1,n+1):
# 	for j in range(1,n+1):
# 		if i == j:
# 			g[i][j] = 0

# for _ in range(m):
# 	a,b,c, = map(int,input().split())
# 	g[a][b] = c


# for k in range(1,n+1):
# 	for i in range(1,n+1):
# 		for j in range(1,n+1):
# 			g[i][j] = min(g[i][j],g[i][k]+g[k][j])

# answer = 0
# answer2 = 0
# for k in range(1,n+1):
# 	for i in range(1,n+1):
# 		for j in range(1,n+1):
# 			answer = min(g[i][2],g[i][k]+g[k][2])
# 			answer2 = min(g[2][i],g[2][k]+g[k][i])
# print(answer+answer2)



import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n,m,x = map(int,input().split())


g = [[] for i in range(n+1)]


for i in range(m):
	a,b,c = map(int,input().split())
	g[a].append((b,c))

def dijkstra(start):
	q = []
	heapq.heappush(q,(0,start))
	distance = [INF] * (n+1)
	distance[start] = 0


	while q:
		dist,now = heapq.heappop(q)
		if distance[now] < dist:
			continue
		for i in g[now]:
			cost = dist + i[1]
			if cost < distance[i[0]]:
			# i[0] == 위치
			# i[1] == 시간
				distance[i[0]] = cost
				heapq.heappush(q,(cost,i[0]))
	return distance

result = 0
for i in range(1, n + 1):
	go = dijkstra(i)
	back = dijkstra(x)

	result = max(result, go[x] + back[i])
print(result)
