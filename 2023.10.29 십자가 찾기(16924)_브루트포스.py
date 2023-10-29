import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr = [list(input().rstrip()) for _ in range(n)]


for i in range(1,n-1):
	for j in range(1,m-1):
		if arr[i][j] == '*':
			cnt = 1
			while arr[i+1][j] == arr[i-1][j] == arr[i][j+1] == arr[i][j-1]:
				print(i,j,cnt, sep=' ')
