import sys
input = sys.stdin.readline

n,m = map(int,input().split())

visited = [0] * (n+1)
arr = [[] for _ in range(n+1)]
for i in range(m):
	a,b = map(int,input().split())
	arr[a].append(b)
	arr[b].append(a)

answer = []
print(arr)
