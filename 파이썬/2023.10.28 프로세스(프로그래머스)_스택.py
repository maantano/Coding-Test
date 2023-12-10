
# priorities =[2, 1, 3, 2]
# location =2
# 1
priorities = [1, 1, 9, 1, 1, 1]
location = 0
# 5

from collections import deque
def solution(priorities,location):
	q = deque(priorities)
	answer = 0
	while q:
		m = max(q)
		l = q.popleft()
		location -=1
		if l == m:
			answer +=1
			if location < 0:
				break
		else:
			q.append(l)
			if location < 0:
				location = len(q)-1
	return answer


def solution(priorities, location):
	queue =  [(i,p) for i,p in enumerate(priorities)]
	answer = 0
	while True:
		cur = queue.pop(0)
		if any(cur[1] < q[1] for q in queue):
			queue.append(cur)
		else:
			answer += 1
			if cur[0] == location:
				return answer

# def solution(priorities,location):
# 	maxIdx = priorities.index(max(priorities))
# 	lL = priorities[:maxIdx]
# 	rL = priorities[maxIdx:]
# 	cnt = 1
# 	if maxIdx > location:
# 		while lL:
# 			a = lL.pop(0)
# 			if a == priorities[location]:
# 				break
# 			cnt+=1
# 		cnt+=len(rL)
# 	else:
# 		while rL:
# 			a = rL.pop()
# 			if a == priorities[location]:
# 				break
# 			cnt	=1
# 	return cnt







print(solution(priorities,location))
