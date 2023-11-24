n = 3
left = 2
right = 5
result = [3,2,2,3]
def solution(n, left, right):
	answer = []

	for i in range(left, right + 1):
		answer.append(max(i // n, i % n) + 1)

	return answer

solution(n, left, right)

#   0 1 2
# 0 1,2,3
# 1 2,2,3
# 2 3,3,3
# 1,2,3 2,2,3 3,3,3
