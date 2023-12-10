import sys
from itertools import combinations
input = sys.stdin.readline

def gcd(x,y):
	while y > 0:
		x,y = y , x % y
	return x

def lcm(x,y):
	return x*y // gcd(x,y)


arr = list(map(int,input().split()))
combi = list(combinations(arr,3))
lcmnum = int(1e9)
for i in combi:
	a,b,c = i
	ab2 =lcm(a,b)
	lcmnum = min(lcm(ab2,c),lcmnum)
print(lcmnum)
