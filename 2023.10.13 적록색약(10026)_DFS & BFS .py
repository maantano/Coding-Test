# 적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다.


# 크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다.

# 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다.
# 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)


import sys
input = sys.stdin.readline

n = int(input())
g = []

for i in range(n):
	g.append(list(map(str,input().rstrip())))
from collections import deque


dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = deque()
visited = [[0]*n for _ in range(n)]

def bfs(x,y):
	q.append((x,y))
	visited[x][y] = 1
	color = g[x][y]
	while q:
		x,y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if  0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and  color == g[nx][ny]:
				visited[nx][ny] = 1
				q.append((nx,ny))
	# return True



result = 0
for i in range(n):
	for j in range(n):
		if not visited[i][j]:
			bfs(i,j)
			result+=1


for i in range(n):
	for j in range(n):
		if g[i][j] == 'G':
			g[i][j] = 'R'

visited = [[0]*n for _ in range(n)]
result2 = 0
for i in range(n):
	for j in range(n):
		if not visited[i][j]:
			bfs(i,j)
			result2+=1
print(result,result2)






