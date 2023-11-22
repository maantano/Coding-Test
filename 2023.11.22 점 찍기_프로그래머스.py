k = 1
d = 5

# def solution(k, d):
# 	answer = 0
# 	arr = [[0]* (d+1) for _ in range(d+1)]
# 	for i in range(0,d+1,k):
# 		for j in range(0,d+1,k):
# 			if (i**2 +j**2)**0.5 <= d:
# 				answer+=1
# 	return answer

import math
def solution(k, d):
	answer = 0
	for x in range(0, d + 1, k):
		res_d = math.floor(math.sqrt(d*d - x*x))
		answer += (res_d // k) + 1
	return answer
