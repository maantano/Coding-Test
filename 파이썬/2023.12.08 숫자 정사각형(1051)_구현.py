import sys
input = sys.stdin.readline

n,m = map(int,input().split())
g = [list(map(int,input().rstrip())) for _ in range(n)]


def find_squre(s):
	for i in range(n-s+1):
		for j in range(m-s+1):
			if g[i][j] == g[i][j+s-1] == g[i+s-1][j] == g[i+s-1][j+s-1]:
				return True
	return False

maxSize = min(n,m)
for i in range(maxSize,0,-1):
	if find_squre(i):
		print(i**2)
		break
