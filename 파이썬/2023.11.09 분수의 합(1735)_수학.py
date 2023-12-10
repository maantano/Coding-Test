import sys
input = sys.stdin.readline



def gcd(x,y):
	while y > 0:
		x,y = y,x%y
	return x
def lcm(x,y):
	return x*y // gcd(x,y)

fl = list(map(int,input().split()))
sl = list(map(int,input().split()))

bg = (fl[0] * sl[1]) + (fl[1] * sl[0])
bm = fl[1] * sl[1]

if gcd(bm,bg) == 1:
	print(bg,bm ,sep=' ')
else:
	print(bg//gcd(bm,bg),bm//gcd(bm,bg) ,sep=' ')



