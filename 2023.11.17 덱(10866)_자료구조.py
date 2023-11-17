import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
q = deque()


for i in range(n):
	word = input().split()
	if word[0] == 'push_back':
		q.append(word[1])
	elif word[0] == 'push_front':
		q.appendleft(word[1])
	elif word[0] == 'front':
		if len(q) > 0:
			print(q[0])
		else:
			print(-1)
	elif word[0] == 'back':
		if len(q) > 0:
			print(q[-1])
		else:
			print(-1)
	elif word[0] == 'pop_front':
		if len(q) <= 0:
			print(-1)
		else:
			print(q.popleft())
	elif word[0] == 'pop_back':
		if len(q) <= 0:
			print(-1)
		else:
			print(q.pop())
	elif word[0] == 'size':
		print(len(q))
	elif word[0] == 'empty':
		if q:
			print(0)
		else:
			print(1)

