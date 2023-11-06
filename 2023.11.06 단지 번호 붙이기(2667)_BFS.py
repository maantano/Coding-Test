# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
visited = [[0] *n for _ in range(n)]
g = []
for i in range(n):
	g.append(list(map(int,input().rstrip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = []
def bfs(g,x,y):
	global answer
	q = deque([(x,y)])
	visited[x][y] = 1
	g[x][y] = 0
	cnt = 1
	while q:
		x,y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if nx <0 or nx >= n or ny < 0 or ny >= n:
				continue

			if g[nx][ny] and not visited[nx][ny]:
				visited[nx][ny] = 1
				g[nx][ny] = 0
				q.append((nx,ny))
				cnt+=1
	answer.append(cnt)

for i in range(n):
	for j in range(n):
		if g[i][j] == 1:
			bfs(g,i,j)

answer.sort()
print(len(answer))
for i in answer:
	print(i)






