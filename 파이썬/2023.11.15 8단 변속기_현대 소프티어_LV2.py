import sys
input = sys.stdin.readline

arr = list(map(int,input().split()))
visited = [0] * (len(arr))
if arr[0] < arr[1]:
	visited[0] = 1
else:
	visited[0] = 0

for i in range(1,len(arr)):
	if arr[i] > arr[i-1]:
		visited[i] = 1
	else:
		visited[i] = 0

if visited.count(1) == len(arr):
	print('ascending')
elif visited.count(0) == len(arr):
	print('descending')
else:
	print('mixed')


