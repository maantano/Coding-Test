
# order= [4, 3, 1, 2, 5]
# result = 2
order= [5, 4, 3, 2, 1]
result = 5
from collections import deque
def solution(order):
	answer = 1
	deliver = [ i for i in range(1,len(order)+1)]

	order = deque(order)
	tmpS = []
	dq = []
	first = order.popleft()
	for i in deliver:
		if first == i:
			dq = deque(deliver[i-1:])
			break
		else:
			tmpS.append(i)
	while order:
		target = order.popleft()
		if target == dq[0]:
			dq.popleft()
			answer+=1
		elif target == tmpS[-1]:
			tmpS.pop()
			answer+=1
		else:
			break
	return answer




def solution(order):
	assist = []
	i = 1
	cnt = 0
	while i != len(order)+1:
		assist.append(i)
		while assist and assist[-1] == order[cnt]:
			cnt += 1
			assist.pop()

		i += 1
	return cnt




	# order =

	# d = dq.popleft()
	# s = tmpS.pop()
	# if d == tmpS.pop():


	# if d == dq.popleft():
print(solution(order))
