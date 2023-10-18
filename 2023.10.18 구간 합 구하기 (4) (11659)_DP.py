
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))

d  = [0]
tmp = 0
for i in arr:
	tmp += i
	d.append(tmp)

for i in range(m):
	x,y = map(int,input().split())
	print(d[y]-d[x-1])

