import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [[] for _ in range(n+1)]
for i in range(m):
	a,b = map(int,input().split())
	arr[b].append(a)

answer = []
maxCnt = 1

from collections import deque
def bfs(start):
	visited = [0] * (n+1)
	q = deque([start])
	visited[start] = 1
	cnt = 1

	while q:
		now = q.popleft()
		for i in arr[now]:
			if not visited[i]:
				visited[i] = 1
				cnt+=1
				q.append(i)
	return cnt

for i in range(1,n+1):
	cnt = bfs(i)
	if maxCnt < cnt:
		maxCnt = cnt
		answer.clear()
		answer.append(i)
	elif maxCnt == cnt:
		answer.append(i)
print(*answer)


