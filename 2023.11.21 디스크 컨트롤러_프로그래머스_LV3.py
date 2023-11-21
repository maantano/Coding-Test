import sys
sys.setrecursionlimit(10**9)
from collections import deque
import heapq


jobs = [[0, 3], [1, 9], [2, 6]]

def solution(jobs):
	answer = []
	l = len(jobs)
	q = []
	jobs.sort(key=lambda x: x[1]-x[0])
	heapq.heappush(q,jobs[0][1]-jobs[0][0])
	answer.append(jobs[0][1]-jobs[0][0])
	for i in range(1,l):
		n1 = heapq.heappop(q)
		answer.append(n1 + jobs[i][1]-jobs[i][0]+jobs[i-1][0])
		heapq.heappush(q,(n1 + jobs[i][1]-jobs[i][0]))

	return sum(answer) // len(answer)
solution(jobs)


import heapq


jobs = [[0, 3], [1, 9], [2, 6]]

def solution(jobs):
	answer, now, i = 0, 0, 0
	start = -1
	heap = []
	while i < len(jobs):
		for j in jobs:
			if start < j[0] <= now:
				heapq.heappush(heap, [j[1], j[0]])

		if len(heap) > 0:
			cur = heapq.heappop(heap)
			start = now
			now += cur[0]
			answer += now - cur[1]
			i += 1
		else:
			now += 1
	return answer // len(jobs)

solution(jobs)
# import heapq

# def solution(jobs):
# 	answer, now, i = 0, 0, 0
# 	start = -1
# 	heap = []

# 	while i < len(jobs):
# 		for j in jobs:
# 			if start < j[0] <= now:
# 				heapq.heappush(heap, [j[1], j[0]])

# 		if len(heap) > 0:
# 			cur = heapq.heappop(heap)
# 			start = now
# 			now += cur[0]
# 			answer += now - cur[1]
# 			i += 1
# 		else:
# 			now += 1

# 	return answer // len(jobs)

# print(solution(jobs))
