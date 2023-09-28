

# f = end
# s = 현재 위치

# g = target

f = 10
s = 1

g = 10

u = 2
d = 1

f,s,g,u,d = map(int,input().split())
visitied = [0] * (f+1)
count = [0] * (f+1)
from collections import deque

def bfs(s):
	q = deque()
	q.append(s)
	visitied[s] = 1
	while q:
		v = q.popleft()
		if g == v:
			return count[g]
		for i in (v+u,v-d):
			if 0 < i <= f and not visitied[i]:
				visitied[i] = 1
				count[i] = count[v] + 1
				q.append(i)
	if count[g] == 0:
		return 'use the stairs'

print(bfs(s))

