# 월드나라에는 N개의 지점이 있고 N개의 지점 사이에는 M개의 도로와 W개의 웜홀이 있다.
# (단 도로는 방향이 없으며 웜홀은 방향이 있다.)

# 웜홀은 시작 위치에서 도착 위치로 가는 하나의 경로인데,
# 특이하게도 도착을 하게 되면 시작을 하였을 때보다 시간이 뒤로 가게 된다.
# 웜홀 내에서는 시계가 거꾸로 간다고 생각하여도 좋다.

# 한 지점에서 출발을 하여서 시간여행을 하기 시작하여 다시 출발을 하였던 위치로 돌아왔을 때,
# 출발을 하였을 때보다 시간이 되돌아가 있는 경우가 있는지 없는지 궁금해졌다.






# 첫 번째 줄에는 테스트케이스의 개수 TC(1 ≤ TC ≤ 5)가 주어진다.
# 두 번째 줄부터 TC개의 테스트케이스가 차례로 주어지는데
# 각 테스트케이스의 첫 번째 줄에는
# 지점의 수 N(1 ≤ N ≤ 500)
# 도로의 개수 M(1 ≤ M ≤ 2500)
# 웜홀의 개수 W(1 ≤ W ≤ 200)이 주어진다.

# S와 E는 연결된 지점의 번호, T는 이 도로를 통해 이동하는데 걸리는 시간을 의미한다.
# S는 시작 지점, E는 도착 지점, T는 줄어드는 시간을 의미한다.

import sys
input = sys.stdin.readline
INF = int(1e9)

tc = int(input())
g = []


def bf(start):
	distance = [INF] * (n+1)
	distance[start] = 0

	for i in range(1,n+1):
		for edge in g:
			cur,next,cost = edge[0],edge[1],edge[2]
			if distance[next] > cost + distance[cur]:
				distance[next] = cost + distance[cur]
				if i == n - 1:
					return True

	return False


for i in range(tc):
	n,m,w = map(int,input().split())

	for _ in range(m):
		s, e, t = map(int, input().split())
		g.append((s, e, t))
		g.append((e, s, t))
	for _ in range(w):
		s,e,t = map(int,input().split())
		g.append((s,e,-t))
	key = bf(1)


	if key:
		print('YES')
	else:
		print('NO')






# key = 0

# for i in range(1,n+1):
# 	if bf(i):
# 		key = 1
# 		break



