import sys
input = sys.stdin.readline


t =  int(input())
for i in range(t):
	d = int(input())
	cnt = 0
	for i in range(1,d):
		if i**2 + i <= d:
			cnt+=1
	print(cnt)
