
from collections import deque
def bfs():
	q = deque()
	q.append((homeX,homeY))
	# mq = deque(g)
	while q:
		x,y = q.popleft()
		if abs(x-concertX) + abs(y-concertY) <= 1000:
			print('happy')
			return
		for i in range(n):
			if not visited[i]:
				nx,ny = g[i]
				if abs(x-nx) + abs(y-ny) <= 1000:
					q.append((nx,ny))
					visited[i] = 1
	print('sad')
	return



t = int(input())
for i in range(t):
	n = int(input())
	homeX,homeY = map(int,input().split())
	g = []
	for j in range(n):
		g.append(list(map(int,input().split())))
	concertX,concertY = map(int,input().split())
	visited = [ 0 for _ in range(n+1)]
	bfs()





# dx = [-1,1,0,0]
# dy = [0,0,-1,1]


# from collections import deque
# def bfs(x,y,marketList,concertX,concertY):
# 	q = deque()
# 	q.append((x,y))
# 	mq = deque(marketList)
# 	while q:
# 		x,y = q.popleft()
# 		mqX,mqY = mq.popleft()
# 		for j in range(1,21):
# 			for i in range(4):
# 				nx = x + (dx[i]*(j*50))
# 				ny = y + (dy[i]*(j*50))
# 				if nx == mqX or ny == mqY:
# 					q.append((nx,ny))
# 					break


# 		if x == concertX and y == concertY:
# 			print('happy')
# 		else:
# 			print('sad')



# t = int(input())

# for i in range(t):
# 	marketList = []
# 	n = int(input())
# 	homeX,homeY = map(int,input().split())
# 	for j in range(n):
# 		marketList.append(map(int,input().split()))
# 	concertX,concertY = map(int,input().split())
# 	bfs(homeX,homeY,marketList,concertX,concertY)


