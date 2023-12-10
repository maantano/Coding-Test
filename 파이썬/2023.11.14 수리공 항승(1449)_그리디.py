
import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())

q = deque(sorted(list(map(int,input().split()))))
cnt=0
while len(q) >1:
	a = q.popleft()
	b = q.popleft()
	if abs(a-b)+1 <=m:
		q.appendleft(a)
	else:
		cnt+=1
		q.appendleft(b)
print(cnt+1)

