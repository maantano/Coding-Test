import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
	a,b = map(int,input().split())
	cnt = 0
	for i in range(a,b+1):
		w = str(i)
		cnt += w.count('0')
	print(cnt)



