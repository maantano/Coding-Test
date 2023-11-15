import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
arr = []

for i in range(m):
	a,b = map(int,input().split())
	arr.append((a,b))

arr.sort(key= lambda x : x[1], reverse=True)
answer = 0
for i in arr:
	a,b = i
	if n >= a:
		n-=a
		answer += a*b
	else:
		answer += b*n
		n = 0
print(answer)
