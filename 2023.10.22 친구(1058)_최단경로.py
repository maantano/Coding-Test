import sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(str,input().rstrip())) for i in range(n)]
visited = [[0] * (n) for i in range(n)]

# for i in range(n):
# 	for j in range(n):
# 		if i == j:
# 			visited[i][j] = 0
for k in range(n):
	for i in range(n):
		for j in range(n):
			if i == j:
				continue
			if arr[i][j] == 'Y' or (arr[i][k] == 'Y' and arr[k][j] == 'Y'):
				visited[i][j] = 1

res = 0
for i in visited:
	res = max(res,sum(i))
print(res)



