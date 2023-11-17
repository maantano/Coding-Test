import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
q = deque(list(i for i in range(1,n+1)))

while len(q) > 1:
	p = q.popleft()
	q.append(q.popleft())
print(q[0])


