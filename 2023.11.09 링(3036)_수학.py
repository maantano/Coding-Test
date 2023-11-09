import sys
input = sys.stdin.readline

t = int(input())
arr = list(map(int,input().split()))

def gcd(x,y):
	while y > 0:
		x,y = y , x % y
	return x

def lcm(x,y):
	return x*y // gcd(x,y)


for i in range(1,t):
	lc = lcm(arr[0],arr[i])
	print( lc // arr[i], lc // arr[0],sep='/')
