import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr = [list(input().rstrip()) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]


for i in range(n):
	for j in range(m):
		if arr[i][j] == '*':
			visited[i][j] = 1

def chk(i,j,size,visited):
	count = 0
	answer = []
	for s in range(1,size+1):
		if arr[i-s][j] == arr[i+s][j] == arr[i][j-s] == arr[i][j+s] == '*' :
			count+=1
			answer = [i+1,j+1,s]
			visited[i][j] = 0
			visited[i-s][j] = 0
			visited[i+s][j] = 0
			visited[i][j-s] = 0
			visited[i][j+s] = 0
		else:
			return 1, answer
	return count,answer
