from collections import deque



prices=[1, 2, 3, 2, 3]
# return = [4, 3, 1, 1, 0]
# def solution(prices):
# 	stack = []
# 	while prices:
# 		cnt = 0
# 		a = prices.pop(0)
# 		for i in range(len(prices)):

# 			if a <= prices[i]:
# 				cnt+=1
# 			if i == len(prices)-1:
# 				stack.append(cnt)

# 	return stack+[0]
# solution(prices)

from collections import deque
def solution(prices):
	answer = []
	q = deque(prices)
	while q:
		p = q.popleft()
		sec = 0
		for i in q:
			sec+=1
			if p > i:
				break
		answer.append(sec)
	print(answer)

solution(prices)

