import sys
input = sys.stdin.readline


a,b,c,d,e,f = map(int,input().split())

y = 0
x = 0
for i in range(-999,1000):
	if (c - (b * i)) // a == (f - (e * i)) // d:
		y = i
	elif (c - (a*i)) // b == (f-(d*i)) // e:
		x = i
	if x !=0 and y !=0:
		break
print(x,y,)

import sys
input = sys.stdin.readline

a,b,c,d,e,f = map(int,input().split())

for i in range(-999,1000):
	for j in range(-999,1000):
		if a*i + b*j == c and d*i + e*j == f:
			print(i,j)
