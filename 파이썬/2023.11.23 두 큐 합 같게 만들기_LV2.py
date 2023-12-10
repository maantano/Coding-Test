
# c
queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]
result = 7
# queue1 = [1, 1]
# queue2 = [1, 5]
# result = -1

# from collections import deque
# def solution(queue1, queue2):
# 	num = (sum(queue1)+ sum(queue2)) // 2
# 	answer = 0
# 	dq1= deque(queue1)
# 	dq2= deque(queue2)
# 	while True:
# 		if sum(dq1) > num:
# 			dq2.append(dq1.popleft())
# 			answer+=1
# 		elif sum(dq1) < num:
# 			dq1.append(dq2.popleft())
# 			answer+=1

# 		if sum(dq1) == num and sum(dq2) == num:
# 			break
# 		elif dq2 == deque(queue1) and dq1 == deque(queue2):
# 			answer =  -1
# 			break

# 	return answer




from collections import deque
def solution(queue1, queue2):
	q1, q2 = deque(queue1), deque(queue2)
	q1_sum, q2_sum = sum(q1), sum(q2)
	for i in range(300000):
		if q1_sum == q2_sum:
			return i
		elif q1_sum > q2_sum:
			num = q1.popleft()
			q2.append(num)
			q1_sum -= num
			q2_sum += num
		else:
			num = q2.popleft()
			q1.append(num)
			q2_sum -= num
			q1_sum += num
	return -1




from collections import deque
def solution(queue1, queue2):
	num = (sum(queue1)+ sum(queue2)) // 2
	answer = 0
	dq1= deque(queue1)
	dq2= deque(queue2)
	while True:
		if sum(dq1) > sum(dq2):
			dq2.append(dq1.popleft())
			answer+=1
		else:
			dq1.append(dq2.popleft())
			answer+=1

		if sum(dq1) == num and sum(dq2) == num:
			break
		if answer == len(dq1) * 4:
			answer = -1
			break
	return answer



solution(queue1, queue2)
