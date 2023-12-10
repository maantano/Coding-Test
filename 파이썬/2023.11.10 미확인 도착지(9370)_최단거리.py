
# #  그들이 g와 h 교차로 사이에 있는 도로를 지나갔다는 것을 알아냈다.

# # 첫 번째 줄에는 테스트 케이스의 T(1 ≤ T ≤ 100)가 주어진다. 각 테스트 케이스마다

# 첫 번째 줄에 3개의 정수 n, m, t (2 ≤ n ≤ 2 000, 1 ≤ m ≤ 50 000 and 1 ≤ t ≤ 100)가 주어진다. 각각 교차로, 도로, 목적지 후보의 개수이다.
# 두 번째 줄에 3개의 정수 s, g, h (1 ≤ s, g, h ≤ n)가 주어진다. s는 예술가들의 출발지이고, g, h는 문제 설명에 나와 있다. (g ≠ h)
# 그 다음 m개의 각 줄마다 3개의 정수 a, b, d (1 ≤ a < b ≤ n and 1 ≤ d ≤ 1 000)가 주어진다. a와 b 사이에 길이 d의 양방향 도로가 있다는 뜻이다.

# 그 다음 t개의 각 줄마다 정수 x가 주어지는데, t개의 목적지 후보들을 의미한다. 이 t개의 지점들은 서로 다른 위치이며 모두 s와 같지 않다.
# 교차로 사이에는 도로가 많아봐야 1개이다. m개의 줄 중에서 g와 h 사이의 도로를 나타낸 것이 존재한다. 또한 이 도로는 목적지 후보들 중 적어도 1개로 향하는 최단 경로의 일부이다.

import sys
input = sys.stdin.readline

import heapq
INF = int(1e9)

def dijstra(start):
	q = []
	heapq.heappush(q,(0,start))
	distance = [INF] * (n+1)
	distance[start] = 0

	while q:
		dist,now= heapq.heappop(q)

		if distance[now] < dist:
			continue
		for node,leaf in arr[now]:
			cost = dist + leaf
			if cost < distance[node]:
				distance[node] = cost
				heapq.heappush(q,(cost,node))
	return distance



t = int(input())
for i in range(t):
	n,m,k = map(int,input().split())
	s,g,h = map(int,input().split())
	arr = [[] for _ in range(n+1)]
	for i in range(m):
		a,b,d = map(int,input().split())
		arr[a].append((b,d))
		arr[b].append((a,d))
	skip = []
	for i in range(k):
		skip.append(int(input()))



	dijs = dijstra(s)
	dijg = dijstra(g)
	dijh = dijstra(h)

	answer = []
	for i in skip:
		if ( dijs[g] + dijg[h] + dijh[i] == dijs[i] ) or ( dijs[h] + dijh[g]+ dijg[i] == dijs[i] ):
			answer.append(i)
	answer.sort()
	print(*answer)


# 테스트 케이스마다

# 입력에서 주어진 목적지 후보들 중 불가능한 경우들을 제외한 목적지들을 공백으로 분리시킨 오름차순의 정수들로 출력한다.

# 2
# 교차로(n),도로(m),목적지(t)
# 5 4 2
# 시작(s),g,h = g,h 교차로 사이에 있는 도로를 지나 갔다
# 1 2 3

# 1 2 6
# 2 3 2
# 3 4 4
# 3 5 3

# 5
# 4



# 6 9 2

# 2 3 1

# 1 2 1
# 1 3 3
# 2 4 4
# 2 5 5
# 3 4 3
# 3 6 2
# 4 5 4
# 4 6 3
# 5 6 7
# 5
# 6
