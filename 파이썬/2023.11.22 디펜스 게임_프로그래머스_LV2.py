
# n = 7
# k = 3
# enemy = [4, 2, 4, 5, 3, 3, 1]





# import heapq
# def solution(n, k, enemy):
# 	h = enemy[:k]
# 	heapq.heapify(h)
# 	# print(h)
# 	for i in range(k,len(enemy)):
# 		n -= heapq.heappushpop(h,enemy[i])
# 		if n < 0:
# 			return i

# print(solution(n, k, enemy))


n = 3
k = 2
enemy = [1,1,1,1]

from heapq import heappush, heappop

def solution(n, k, enemy):
	stage = len(enemy)
	if k >= stage :
		return stage
	q = []

	for i in range(stage) :
		heappush(q, enemy[i])
		if len(q) > k :
			last = heappop(q)
			if last > n :
				return i
			n -= last

	return stage

print(solution(n, k, enemy))
