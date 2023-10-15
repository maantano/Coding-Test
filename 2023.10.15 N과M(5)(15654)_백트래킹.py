n,m = map(int,input().split())


arr = list(map(int,input().split()))
arr.sort()

answer = []

def dfs(d,i):

	if d == m:
		print(*answer)
		return
	for i in range(n):
		if answer.count(arr[i]):
			continue
		answer.append(arr[i])
		dfs(d+1,i+1)
		answer.pop()






dfs(0,0)
