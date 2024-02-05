# [0,0] => [500,500]

# 잃는 생명의 최솟값


import sys
input = sys.stdin.readline
from collections import deque

danger = []
death = []
N = int(input())
for _ in range(N):
	X1, Y1, X2, Y2 = map(int, input().split())
	danger.append((X1, Y1, X2, Y2))

M = int(input())
for _ in range(M):
	X1, Y1, X2, Y2 = map(int, input().split())
	death.append((X1, Y1, X2, Y2))

graph = [[0] * 501 for _ in range(501)]
for i in range(501):
	for j in range(501):
		# 위험 영역에 속한다면
		for a1, b1, a2, b2 in danger:
			if (min(a1, a2) <= i <= max(a1, a2)) and (min(b1, b2) <= j <= max(b1, b2)):
				graph[i][j] = 1
		# 죽음 영역에 속한다면
		for a1, b1, a2, b2 in death:
			if (min(a1, a2) <= i <= max(a1, a2)) and (min(b1, b2) <= j <= max(b1, b2)):
				graph[i][j] = 2


answer = 0
visit = [[False] * 501 for _ in range(501)]
q = deque()
q.append((0, 0, 0))
visit[0][0] = True
can_reach = False

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while q:
	x,y,life = q.popleft()

	if x == 500 and y == 500:
		can_reach = True
		answer = life
		break
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]

		if 0<= nx < 501 and 0<= ny < 501:
			if not visit[nx][ny]:
				visit[nx][ny] = 1
				if not graph[nx][ny]:
					q.append((nx,ny,life))
				else:
					q.append((nx,ny,life+1))

if can_reach:
	print(answer)
else:
	print(-1)


