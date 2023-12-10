food = [1, 7, 1, 2]
result = "1223330333221"

def solution(food):
	arr = food[1:]
	answer =[]
	for i in range(len(arr)):
		if arr[i] !=1:
			answer.append((arr[i] // 2) * str(i+1))
	return ''.join(answer)+'0'+''.join(sorted(answer,reverse=True))

print(solution(food))


def solution(food):
	answer = ''
	for i,n in enumerate(food[1:]):
		answer += str(i+1) * (n//2)
	return answer + "0" + answer[::-1]
