for _ in range(m):
	a,b,c = map(int,input().split())
	arr[a][b] = c
	arr[b][a] = c
	res[a][b] = b
	res[b][a] = a

for i in range(1,n+1):
	for j in range(1,n+1):
		if i == j:
			arr[i][j] = 0
			res[i][j] = INF
for k in range(1,n+1):
	for i in range(1,n+1):
		for j in range(1,n+1):
			if arr[i][j] > arr[i][k] + arr[k][j]:
				arr[i][j] = arr[i][k] + arr[k][j]
				res[i][j] = res[i][k]

for i in range(1, n + 1):
	for j in range(1, n + 1):
		if res[i][j] == INF:
			print('-', end=' ')
		else:
			print(res[i][j], end=' ')
	print()

