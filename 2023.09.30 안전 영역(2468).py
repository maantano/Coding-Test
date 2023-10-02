
from collections import deque

n = int(input())
arr = []
maxNum = 0
for i in range(n):
	arr.append(list(map(int,input().split())))
	for j in range(n):
		if arr[i][j] > maxNum:
			maxNum = arr[i][j]
print('maxNum =====>',maxNum)

move = [
	[1,0],
	[-1,0],
	[0,1],
	[0,-1],
]
def bfs(x,y,limit,visited):

	q = deque()
	q.append((x,y))
	visited[x][y] = 1
	while q:
		popX,popY = q.popleft()

		for i in range(4):
			moveX,moveY= move[i]
			newX = popX + moveX
			newY = popY + moveY
			if 0 <= newX < n and 0 <= newY < n:
				if arr[newX][newY] > limit and visited[newX][newY] == 0:
					visited[newX][newY] = 1
					q.append((newX,newY))

result = 0
for i in range(maxNum):
	visited = [[0] * n for _ in range(n)]
	cnt = 0

	for j in range(n):
		for k in range(n):
			if arr[j][k] > i and visited[j][k] == 0:
				bfs(j,k,i,visited)
				cnt+=1
	if result < cnt:
		result = cnt

print(result)
# for i in range(1,n):
# 	print(bfs(0,0,i))
# 	print('-------------------------')




# def dfs(x,y):
# 	for i in range(n):
# 		if visited[x][y] == 1:
# 			continue
# 		moveX = move[i][0]
# 		moveY = move[i][1]
# 		newX = moveX + x
# 		newY = moveY + y
# 		if newX < 0 or newX >= n or newY < 0 or newY >= n:
# 			continue
# 		if visited[x][y] == 0:
# 			visited[x][y] = 1
# 			dfs(newX,newY)






