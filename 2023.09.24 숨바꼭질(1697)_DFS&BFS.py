N,K = map(int,input().split())
MAX = [0] * (100000+1)

from collections import deque

def bfs(x,k):
	q = deque()
	q.append(x)
	while q:
		x= q.popleft()
		if x == k:
			print(MAX[x])
			return
		for j in (x-1,x+1,x*2):
			if 0 <= j <= 100000 and not MAX[j]:
				MAX[j] = MAX[x] + 1
				q.append(j)


bfs(N,K)
