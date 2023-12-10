import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
visited = [0] * (n)

answer = []

def bt(idx,n,m):
	if idx == m:
		print(' '.join(map(str,answer)))
		return
	overlap = 0
	for i in range(n):
		if not visited[i] and overlap != arr[i]:
			visited[i] = 1
			answer.append(arr[i])
			overlap = arr[i]
			bt(idx+1,n,m)
			visited[i] = 0
			answer.pop()
bt(0,n,m)
