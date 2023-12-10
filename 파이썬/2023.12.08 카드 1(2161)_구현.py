import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = deque([i for i in range(1,n+1)])
answer = []
while True:
	if len(arr)==1:
		break
	else:
		answer.append(arr.popleft())
		arr.append(arr.popleft())
answer+=arr
print(*(answer))
