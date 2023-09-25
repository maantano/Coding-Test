N,M = map(int,input().split())
Max = [0] * 100001
from collections import deque

count=0
way = 0

def bfs(x,y):
	global count
	global way
	q = deque()
	q.append(x)
	while q:
		x = q.popleft()
		if x == y:
			# print(Max[x])
			way+=1
			count+=1
			continue
		for i in (x-1,x+1,x*2):
			if Max[i] == 0 or Max[i] == Max[x] + 1:
				Max[i] = count + 1
				q.append(i)

bfs(N,M)
print(count)
print(way)
