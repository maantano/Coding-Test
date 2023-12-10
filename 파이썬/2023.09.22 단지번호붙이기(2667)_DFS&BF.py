n = 7

# n = int(input())
g=[
[0,1,1,0,1,0,0],
[0,1,1,0,1,0,1],
[1,1,1,0,1,0,1],
[0,0,0,0,1,1,1],
[0,1,0,0,0,0,0],
[0,1,1,1,1,1,0],
[0,1,1,1,0,0,0],
]

# g = [[]*n for _ in range(n)]
# for i in range(n):
# 	g=list(map(int,input()))


path = [
	[-1,0],
	[1,0],
	[0,-1],
	[0,1],
]

from collections import deque
def bfs(g,x,y):
	n = len(g)
	q = deque()
	q.append((x,y))
	g[x][y] = 0
	count = 1
	while q:
		start_x,start_y = q.popleft()
		for p in range(4):
			move_x,move_y= path[p]
			newX = start_x + move_x
			newY = start_y + move_y
			if newX <= -1 or newX >= n or newY <= -1 or newY >= n:
				continue
			if g[newX][newY] == 1:
				# g[newX][newY] = g[start_x][start_y] + 1
				g[newX][newY] = 0
				q.append((newX,newY))
				count+=1
	return count
cnt = []
for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            cnt.append(bfs(g, i, j))
cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])

	# for i in range(n):
	# 	for j in range(n):

			# if g[i][j] == continue:

