import sys

t,n,m = map(int,input().split())

cnt = 0

while n != m:
	n -= n // 2
	m -= m // 2
	cnt+=1
print(cnt)


