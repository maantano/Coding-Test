import sys
input = sys.stdin.readline

# numbers = [9, 1, 5, 3, 6, 2]
numbers = [2, 3, 3, 5]
def solution(numbers):
	stack = []
	answer = [-1] * len(numbers)

	for i in range(len(numbers)):
			while stack and numbers[stack[-1]] < numbers[i]:
				answer[stack.pop()] = numbers[i]
			stack.append(i)

	return answer




print(solution(numbers))
# import sys
# input = sys.stdin.readline

# numbers = [9, 1, 5, 3, 6, 2]

# def solution(numbers):
# 	answer = []
# 	for i in range(len(numbers)-1):
# 		if numbers[i] > max(numbers[i+1:]):
# 			answer.append(-1)
# 			continue
# 		for j in range(i,len(numbers)):
# 			if numbers[i] < numbers[j]:
# 				answer.append(numbers[j])
# 				break
# 	return answer +[-1]


# print(solution(numbers))

