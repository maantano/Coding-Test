import sys
input = sys.stdin.readline

n,m = map(int,input().split())
INF = int(1e9)
arr = [[INF] * (n +1) for _ in range(n+1)]
for i in range(1,n+1):
	for j in range(1,m+1):
		if i == j:
			arr[i][j] = 0

for i in range(m):
	a,b,c = map(int,input().split())
	arr[a][b] = c

for k in range(1,n+1):
	for i in range(1,n+1):
		for j in range(1,n+1):
			arr[i][j]= min(arr[i][j],arr[i][k] + arr[k][j])

k = int(input())


city = list(map(int,input().split()))
result = []

for x in range(1,n+1):
	max_result = 0
	for i in city:
		if i != x and arr[i][x] != INF and arr[x][i] != INF:
			max_result = max(max_result,arr[i][x]+arr[x][i])
	result.append(max_result)


min_result = min(result)
for i in range(n):
	if result[i] == min_result:
		print(i+1, end=' ')
