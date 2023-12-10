import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
answer = []
def dfs(start):
	if len(answer) == m:
		print(*answer)
		return
	for i in range(start,n):
		answer.append(arr[i])
		dfs(i)
		answer.pop()
dfs(0)
