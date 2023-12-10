

bridge_length=2
weight=10
truck_weights =[7,4,5,6]

from collections import deque
def solution(bridge_length, weight, truck_weights):
	q = deque(truck_weights)
	b = deque([0] * bridge_length)
	time = 0
	curW = 0
	while q:

		time+=1
		curW -= b.popleft()
		if curW + q[0] <= weight:
			curW += q[0]
			b.append(q.popleft())
		else:
			b.append(0)
	time += bridge_length
	return time



solution(bridge_length, weight, truck_weights)
