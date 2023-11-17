

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for i in range(t):
	n,target = map(int,input().split())
	q = deque(list(map(int,input().split())))
	cnt = 0
	while q:
		best = max(q)
		front = q.popleft()
		target -=1
		if best == front:
			cnt+=1
			if target <0:
				print(cnt)
				break
		else:
			q.append(front)
			if target < 0:
				target =len(q)-1

