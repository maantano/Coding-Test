import sys
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
g = [list(map(int,input().split())) for _ in range(5)]

answer = []
def dfs(x,y,idx,l,word):

	if idx == 6:
		answer.append(''.join(l))
		return ''.join(l)
	else:
		for k in range(4):
			nx = x + dx[k]
			ny = y + dy[k]
			if 0<= nx < 5 and 0<= ny < 5:
				dfs(nx,ny,idx+1,l+[word],str(g[nx][ny]))

for i in range(5):
	for j in range(5):
		dfs(i,j,0,[],str(g[i][j]))
print(len(list(set(answer))))





# from collections import deque

# grid = [list(input().split()) for _ in range(5)]
# drs, dcs = [-1, 0, 1, 0], [0, 1, 0, -1]
# res = set()


# def in_range(r, c):
# 	return 0 <= r < 5 and 0 <= c < 5


# def bfs(r, c):
# 	dq = deque()
# 	dq.append((r, c, grid[r][c]))  # r, c ,길이

# 	while dq:
# 		cr, cc, s = dq.popleft()
# 		if len(s) == 6:
# 			res.add(s)
# 			continue

# 		for dr, dc in zip(drs, dcs):
# 			nr = cr + dr
# 			nc = cc + dc

# 			if not in_range(nr, nc):
# 				continue

# 			dq.append((nr, nc, s + grid[nr][nc]))


# # bfs(3, 3)
# for a in range(5):
# 	for b in range(5):
# 		bfs(a, b)
# print(len(sorted(res)))
