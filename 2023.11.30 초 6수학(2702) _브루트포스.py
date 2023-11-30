import sys
input = sys.stdin.readline

def gcd(x,y):
	while y>0:
		x,y = y,x%y
	return x

def lcm(x,y):
	return x*y // gcd(x,y)

n = int(input())
for i in range(n):
	x,y = map(int,input().split())
	print(lcm(x,y),gcd(x,y),sep=' ')
