N,K = map(int,input().split())
# N = 5
# K = 17
from collections import deque

Max = 100000
visited = [0] * (Max+1)




# def bfs(x,y):
q = deque()
q.append(N)
answerWay = 0
answerCnt = 0

while q:
	x = q.popleft()
	count = visited[x]
	if x == K:
		answerCnt = count
		answerWay +=1
		continue

	for i in (x-1,x+1,x*2):
		if 0 <= i < Max:
			if visited[i] == 0 or visited[i] == visited[x]+1:
				q.append(i)
				visited[i] = count +1

print(answerCnt)
print(answerWay)

