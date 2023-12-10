# from collections import deque
# import sys
# input = sys.stdin.readline
# INF = int(1e9)
# n = int(input())
# arr = [[INF]*(n+1) for _ in range(n+1)]


# for i in range(n):
# 	a,b = map(int,input().split())
# 	if a == -1 and b == -1:
# 		break
# 	arr[a][b] = 1
# 	arr[b][a] = 1
# for i in range(1,n+1):
# 	for j in range(1,n+1):
# 		if i == j:
# 			arr[i][j] = 0


# for k in range(1,n+1):
# 	for i in range(1,n+1):
# 		for j in range(1,n+1):
# 			if arr[i][j] == 1 or arr[i][j] == 0:
# 				continue
# 			elif arr[i][j] > arr[i][k]+arr[k][j]:
# 				arr[i][j] = arr[i][k]+arr[k][j]

# r = []

# for i in range(1,n+1):
# 	r.append(max(arr[i][1:]))
# m = min(r)
# print(m, r.count(m))
# for i,v in enumerate(r):
# 	if v == m:
# 		print(i+1,end = ' ')






import sys
from collections import deque
input = sys.stdin.readline

def bfs(n):
	print(n)


