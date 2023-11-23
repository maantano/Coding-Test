want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
result = 3

from collections import Counter
def solution(want, number, discount):
	answer = 0
	target = dict(zip(want,number))
	dl = len(discount)
	for i in range(0,dl-9):
		if Counter(discount[i:i+10]) == target:
			answer+=1
	return answer

solution(want, number, discount)
