import sys
input = sys.stdin.readline

n = int(input().rstrip())
stats = [list(map(int,input().split())) for _ in range(n)]
visited = [0] * n
ans = sys.maxsize

def is_it():
	global ans
	start,link = 0,0
	for i in range(n-1):
		for j in range(i+1,n):
			if visited[i] and visited[j]:
				start += stats[i][j]
			elif not visited[i] and not visited[j]:
				link += stats[i][j]
	ans = min(ans,abs(start-link))
	return

def resolve(iter):

	if iter == n:
		is_it()
		return
	visited[iter] = 1
	resolve(iter+1)
	visited[iter] = 0
	resolve(iter+1)
resolve(0)
print(ans)









