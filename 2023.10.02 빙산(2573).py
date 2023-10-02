n = 5
m = 7
arr = [
	[0,0,0,0,0,0,0],
	[0,2,4,5,3,0,0],
	[0,3,0,2,5,2,0],
	[0,7,6,2,4,0,0],
	[0,0,0,0,0,0,0],
]


# n,m = map(int,input().split())
# arr = [[0] * 7 for _ in range(n) ]
# for i in range(n):
# 	arr[i] = list(map(int,input().split()))




from collections import deque
visited = [[0] * 7 for _ in range(n) ]

move = [
	[1,0],
	[-1,0],
	[0,1],
	[0,-1],
]
def bfs(x,y):
	q = deque()
	q.append((x,y))
	visited[x][y] = 1

	while q:
		popX,popY = q.popleft()
		for i in range(4):
			moveX,moveY = move[i]
			newX = popX + moveX
			newY = popY + moveY
			if newX <= 0 or newX >=n or newY <= 0 or newY >=n:
				continue
			# if visited[newX][newY] == 1:
			# 	continue
			if arr[newX][newY] == 0:
				arr[newX][newX] -= 1
				q.append((newX,newY))





