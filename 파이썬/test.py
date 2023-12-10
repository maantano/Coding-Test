# 5 17

# 4

N,M = map(int,input().split())

Max = 10000
arr = [0] * (Max+1)


from collections import deque
def bfs(x,y):
	q = deque()
	q.append(x)
	while q:
		x = q.popleft()
		if x == y:
			print(arr[x])
			return
		for i in (x-1,x+1,x*2):
			if 0 <= i <= Max and not arr[i]:
				arr[i] = arr[x] + 1
				q.append(i)

bfs(N,M)
