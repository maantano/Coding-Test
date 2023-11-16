import sys
input = sys.stdin.readline
t = int(input())


from collections import deque
def bfs(start):
	q = deque([start])
	visited[start] = 1
	cnt = 0
	while q:
		node = q.popleft()
		for i in arr[node]:
			if not visited[i]:
				visited[i] = 1
				q.append(i)
				cnt+=1
	return cnt


for i in range(t):
	n,m = map(int,input().split())
	arr = [[] for _ in range(n+1)]
	visited = [0] * (n+1)

	for _ in range(m):
		a,b = map(int,input().split())
		arr[a].append(b)
		arr[b].append(a)
	minCnt = int(1e9)
	print(bfs(1))

