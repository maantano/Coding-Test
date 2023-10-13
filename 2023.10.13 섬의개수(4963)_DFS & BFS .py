dx = [-1,1,0,0]
dy = [0,0,-1,1]

dzx = [0,0,-1,1]
dzy = [-1,1,0,0]

# dz = [-1,1,-1,1]

from collections import deque
def chk(x,y):
	q = deque([(x,y)])
	visited[x][y] = 1

	while q:
		popX,popY = q.popleft()

		for i in range(4):
			nx = popX + dx[i]
			ny = popY + dy[i]

			for i in range(4):
				nzx = nx + dzx[i]
				nzy = ny + dzy[i]

				if (0 <= nx < y and 0 <= ny < x):
					if not visited[nx][ny] and arr[nx][ny] == 1:
						visited[nx][ny] = 1
						q.append((nx,ny))
					elif not visited[nzx][nzy] and (visited[nzx][nzy] == 1):
						visited[nzx][nzy] = 1
						q.append((nzx,nzy))
	return True

answer = []
while True:
	n,m = map(int,input().split())
	cnt = 0
	if n == 0 and m == 0:
		break
	arr = []
	for i in range(m):
		arr.append(list(map(int,input().split())))
	visited = [[0] * n for _ in range(n)]
	for i in range(m):
		for j in range(n):
			if arr[i][j] == 1:
				cnt+=chk(i,j)
	answer.append(cnt)

print(answer)
for i in answer:
	print(i)





