import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
	n,m = map(int,input().split())
	cnt = 0
	for j in range(1,n+1):
		for k in range(j+1,n):
			if (j**2 + k**2 + m) % (j*k) == 0:
				cnt+=1
	print(cnt)
