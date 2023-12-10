import sys
input = sys.stdin.readline

# 5 17
n,m = map(int,input().split(' '))
from collections import deque
Max = 100000
visited = [0] * (Max+1)
move = [0] * (Max + 1)


def path(x):
	arr = []
	tmp = x
	for _ in range(visited[x]+1):
		arr.append(tmp)
		tmp = move[tmp]
	print(' '.join(map(str,arr[::-1])))

answer = []
def bfs(n,m):
	q = deque([n])
	while q:
		x = q.popleft()
		if x == m:
			print(visited[x])
			path(x)
			return
		for i in x-1,x+1,x*2:
			if  0 <= i <= Max  and not visited[i]:
				visited[i] = visited[x] + 1
				q.append(i)
				move[i] = x
bfs(n,m)
