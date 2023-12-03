import sys
input = sys.stdin.readline


n,m = map(int,input().split())

g = [list(map(int,input().rstrip())) for _ in range(n)]

def findS(s):
	for i in range(n-s+1):
		for j in range(m-s+1):
			if g[i][j] == g[i][j+s-1] == g[i+s-1][j] == g[i+s-1][j+s-1]:
				return True
		return False


for i in range(min(n,m),-1,-1):
	print(i)
	if findS(i):
		print(i**2)
		break
