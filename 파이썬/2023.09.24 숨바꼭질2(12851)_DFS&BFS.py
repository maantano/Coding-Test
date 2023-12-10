N,K = map(int,input().split())
# N = 5
# K = 17
from collections import deque

Max = 20
visited = [0] * (Max+1)




# def bfs(x,y):
q = deque()
q.append(N)
answerWay = 0
answerCnt = 0

while q:
	x = q.popleft()
	count = visited[x]

	print('x ====>',x)
	if x == K:
		answerCnt = count
		answerWay +=1
		continue

	for i in (x-1,x+1,x*2):
		if 0 <= i < Max:
			if visited[i] == 0 or visited[i] == visited[x]+1:
				print('i ====>',i)
				print('x ====>',x)
				print('visited[',i,'] ====>',visited[i])
				print('visited[',x,'] ====>',visited[x])

				q.append(i)
				print('q ====>',q)
				print('========================================')

				visited[i] = count +1

print(visited)
print(answerCnt)
print(answerWay)

