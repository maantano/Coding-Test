import sys
input = sys.stdin.readline
import heapq


n,m,r  = map(int,input().split())
t = [0]+list(map(int,input().split()))
INF = int(1e9)
arr = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(r):
	a,b,c = map(int,input().split())
	arr[a][b] = c
	arr[b][a] = c

for i in range(n+1):
	arr[i][i] = 0


for k in range(1,n+1):
	for i in range(1,n+1):
		for j in range(1,n+1):
			arr[i][j] = min(arr[i][k]+ arr[k][j],arr[i][j])

ans = 0

for i in range(1,n+1):
	tmp = 0
	for j in range(1,n+1):
		if arr[i][j] <= m:
			tmp += t[j]
	ans = max(ans,tmp)
print(ans)


