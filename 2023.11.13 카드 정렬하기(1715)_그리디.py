import sys
import heapq
input = sys.stdin.readline

q = []
n = int(input())

for i in range(n):
	heapq.heappush(q,int(input()))

if len(q) == 1:
	print(0)
else:
	answer = 0
	while len(q) > 1:
		a = heapq.heappop(q)
		b = heapq.heappop(q)
		answer += a+b
		heapq.heappush(q,(a+b))
	print(answer)
