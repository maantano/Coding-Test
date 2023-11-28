import sys; input = sys.stdin.readline

def dfs(r, c, idx, total):
	global ans
	if ans >= total + max_val * (3 - idx):
		return
	if idx == 3:
		ans = max(ans, total)
		return
	else:
		for i in range(4):
			nr = r + dr[i]
			nc = c + dc[i]
			if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
				if idx == 1:
					visit[nr][nc] = 1
					dfs(r, c, idx + 1, total + arr[nr][nc])
					visit[nr][nc] = 0
				visit[nr][nc] = 1
				dfs(nr, nc, idx + 1, total + arr[nr][nc])
				visit[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0
max_val = max(map(max, arr))

for r in range(N):
	for c in range(M):
		visit[r][c] = 1
		dfs(r, c, 0, arr[r][c])
		visit[r][c] = 0

print(ans)


n,m = map(int,input().split())
visited = [[0] * m for _ in range(n)]
g = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0

def dfs(x,y,idx,total):
	global ans
	if idx == 3:
		if total > ans:
			ans = total
	else:
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0<= nx <n and 0<= ny < m:
				if not visited[nx][ny]:
					visited[nx][ny] = 1
					dfs(nx,ny,idx+1,total+g[nx][ny])
					visited[nx][ny] = 0


def block(x,y,total):
	global ans
	make_block = 0
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if 0<= nx <n and 0<= ny < m:
			make_block +=1
			total+=g[nx][ny]
	if make_block == 3:
		if total > ans:
			ans = total
	if make_block ==4:
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			total -= g[nx][ny]
			if total > ans:
				ans = total
			total+=g[nx][ny]

for i in range(n):
	for j in range(m):
		visited[i][j] = 1
		dfs(i,j,0,g[i][j])
		block(i,j,g[i][j])
		visited[i][j] = 0
print(ans)
