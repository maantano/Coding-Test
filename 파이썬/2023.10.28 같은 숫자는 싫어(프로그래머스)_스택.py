arr = [1,1,3,3,0,1,1]
# answer = [1,3,0,1]

# arr = [4,4,4,3,3]
# answer = [4,3]



def solution(arr):
	stack  = []
	for i in arr:
		if stack[-1:] == [i]: continue
		stack.append(i)
	return stack


print(solution(arr))
